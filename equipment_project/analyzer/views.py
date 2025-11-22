import pandas as pd
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Upload
from .serializers import UploadSerializer
from django.contrib.auth.models import User
from rest_framework import status


# -----------------------------
# USER REGISTER
# -----------------------------
@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already taken"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)

    return Response(
        {
            "message": "User registered successfully",
            "token": token.key
        },
        status=status.HTTP_201_CREATED
    )



# -----------------------------
# LOGIN VIEW
# -----------------------------
@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Invalid credentials"}, status=400)

    token, _ = Token.objects.get_or_create(user=user)

    # last 5 uploads
    uploads = Upload.objects.filter(user=user).order_by("-uploaded_at")[:5]
    uploads_data = UploadSerializer(uploads, many=True).data

    return Response({
        "token": token.key,
        "last_uploads": uploads_data
    })



# -----------------------------
# CSV UPLOAD
# -----------------------------

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    file = request.FILES.get("file")

    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    # Load CSV
    df = pd.read_csv(file)

    # Normalize column names (remove spaces, lowercase)
    df.columns = [c.strip().replace(" ", "").lower() for c in df.columns]

    # Flexible column mapping
    column_map = {
        "equipment": ["equipment", "equipmentname", "equipment_name"],
        "type": ["type"],
        "flowrate": ["flowrate", "flow_rate"],
        "pressure": ["pressure"],
        "temperature": ["temperature", "temp"],
    }

    final_cols = {}

    # Match real columns to standard names
    for standard, possible_names in column_map.items():
        found_col = None
        for col in df.columns:
            if col.lower() in possible_names:
                found_col = col
                break
        if not found_col:
            return Response({"error": f"Missing required column '{standard}'"}, status=400)
        final_cols[standard] = found_col

    # Rename DF columns to standard names
    df = df.rename(columns=final_cols)

    # Ensure numeric conversion
    df["flowrate"] = pd.to_numeric(df["flowrate"], errors="coerce")
    df["pressure"] = pd.to_numeric(df["pressure"], errors="coerce")
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")

    df = df.dropna()

    # -------------------------------
    # OVERALL STATISTICS
    # -------------------------------
    total_records = len(df)
    avg_flowrate = float(df["flowrate"].mean())
    avg_pressure = float(df["pressure"].mean())
    avg_temperature = float(df["temperature"].mean())
    type_distribution = df["type"].value_counts().to_dict()

    # -------------------------------
    # PER-TYPE STATISTICS
    # -------------------------------
    grouped_stats = {}

    for t, group in df.groupby("type"):
        grouped_stats[t] = {
            "count": len(group),
            "avg_flowrate": float(group["flowrate"].mean()),
            "avg_pressure": float(group["pressure"].mean()),
            "avg_temperature": float(group["temperature"].mean()),
        }

    # SAVE To database
    upload = Upload.objects.create(
        user=request.user,
        file_name=file.name,
        total_records=total_records,
        avg_flowrate=avg_flowrate,
        avg_pressure=avg_pressure,
        avg_temperature=avg_temperature,
        type_distribution=type_distribution,
         per_type_stats=grouped_stats,
    )

    serializer = UploadSerializer(upload)

    # -------------------------------
    # FINAL RESPONSE
    # -------------------------------
    return Response({
        "message": "File processed successfully",
        "overall_stats": {
            "total_records": total_records,
            "avg_flowrate": avg_flowrate,
            "avg_pressure": avg_pressure,
            "avg_temperature": avg_temperature,
            "type_distribution": type_distribution
        },
        "per_type_stats": grouped_stats,
        "data": serializer.data
    }, status=201)
