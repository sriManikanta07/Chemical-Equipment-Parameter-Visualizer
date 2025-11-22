import React, { useState, useEffect, useRef } from 'react';
import * as Chart from 'chart.js';

const API_BASE_URL = 'https://equipmentanalyzer.pythonanywhere.com/api';

// Register ALL Chart.js components including controllers
Chart.Chart.register(
  Chart.ArcElement,
  Chart.Tooltip,
  Chart.Legend,
  Chart.CategoryScale,
  Chart.LinearScale,
  Chart.BarElement,
  Chart.Title,
  Chart.LineElement,
  Chart.PointElement,
  Chart.PieController,  // Added PieController
  Chart.BarController   // Added BarController
);

// Login Component
const Login = ({ onLogin, onSwitchToRegister }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!username || !password) {
      setError('Please enter username and password');
      return;
    }

    setError('');
    setLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/login/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || 'Login failed');
      }

      localStorage.setItem('token', data.token);
      onLogin(data);
    } catch (err) {
      setError(err.message || 'Login failed. Please check your credentials.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="bg-white p-8 rounded-lg shadow-xl w-96">
        <h2 className="text-3xl font-bold text-center mb-6 text-gray-800">Login</h2>
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}
        <div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Username
            </label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSubmit()}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSubmit()}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline disabled:opacity-50"
          >
            {loading ? 'Logging in...' : 'Login'}
          </button>
        </div>
        <div className="text-center mt-4">
          <button
            onClick={onSwitchToRegister}
            className="text-blue-500 hover:text-blue-700 text-sm"
          >
            Don't have an account? Register
          </button>
        </div>
      </div>
    </div>
  );
};

// Register Component
const Register = ({ onRegister, onSwitchToLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!username || !password) {
      setError('Please enter username and password');
      return;
    }

    setError('');
    setLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/register/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || 'Registration failed');
      }

      localStorage.setItem('token', data.token);
      onRegister(data);
    } catch (err) {
      setError(err.message || 'Registration failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-50 to-teal-100">
      <div className="bg-white p-8 rounded-lg shadow-xl w-96">
        <h2 className="text-3xl font-bold text-center mb-6 text-gray-800">Register</h2>
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}
        <div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Username
            </label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSubmit()}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <div className="mb-6">
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Password
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSubmit()}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            />
          </div>
          <button
            onClick={handleSubmit}
            disabled={loading}
            className="w-full bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline disabled:opacity-50"
          >
            {loading ? 'Registering...' : 'Register'}
          </button>
        </div>
        <div className="text-center mt-4">
          <button
            onClick={onSwitchToLogin}
            className="text-green-500 hover:text-green-700 text-sm"
          >
            Already have an account? Login
          </button>
        </div>
      </div>
    </div>
  );
};

// Sidebar Component
const Sidebar = ({ uploads, selectedFile, onSelectFile }) => {
  return (
    <div className="w-64 bg-gray-800 text-white h-screen overflow-y-auto">
      <div className="p-4">
        <h3 className="text-xl font-bold mb-4">Recent Uploads</h3>
        {uploads.length === 0 ? (
          <p className="text-gray-400 text-sm">No uploads yet</p>
        ) : (
          <ul>
            {uploads.map((upload) => (
              <li
                key={upload.id}
                onClick={() => onSelectFile(upload)}
                className={`p-3 mb-2 rounded cursor-pointer transition ${
                  selectedFile?.id === upload.id 
                    ? 'bg-blue-600 hover:bg-blue-700 shadow-lg' 
                    : 'bg-gray-700 hover:bg-gray-600'
                }`}
              >
                <div className="font-semibold truncate">{upload.file_name}</div>
                <div className="text-xs text-gray-400">
  {upload.uploaded_at ? upload.uploaded_at.split('.')[0].replace('T', ' ') : ''}
</div>

              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

// Upload CSV Component
const UploadCSV = ({ onUploadSuccess }) => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError('');
  };

  const handleSubmit = async () => {
    if (!file) {
      setError('Please select a file');
      return;
    }

    setLoading(true);
    setError('');

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(`${API_BASE_URL}/upload_csv/`, {
        method: 'POST',
        headers: {
          'Authorization': `Token ${localStorage.getItem('token')}`
        },
        body: formData
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || 'Upload failed');
      }

      onUploadSuccess(data);
      setFile(null);
      if (fileInputRef.current) {
        fileInputRef.current.value = '';
      }
    } catch (err) {
      setError(err.message || 'Upload failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-lg mb-6">
      <h3 className="text-2xl font-bold mb-4 text-gray-800">Upload CSV File</h3>
      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}
      <div>
        <div className="mb-4">
          <input
            ref={fileInputRef}
            type="file"
            accept=".csv"
            onChange={handleFileChange}
            className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
          />
        </div>
        <button
          onClick={handleSubmit}
          disabled={loading || !file}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline disabled:opacity-50"
        >
          {loading ? 'Uploading...' : 'Upload'}
        </button>
      </div>
    </div>
  );
};

// Pie Chart Component - FIXED
const PieChart = ({ data }) => {
  const canvasRef = useRef(null);
  const chartRef = useRef(null);

  useEffect(() => {
    if (!canvasRef.current) return;

    // Destroy existing chart before creating new one
    if (chartRef.current) {
      chartRef.current.destroy();
      chartRef.current = null;
    }

    const ctx = canvasRef.current.getContext('2d');
    
    try {
      chartRef.current = new Chart.Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'bottom',
            }
          }
        }
      });
    } catch (error) {
      console.error('Error creating pie chart:', error);
    }

    // Cleanup function
    return () => {
      if (chartRef.current) {
        chartRef.current.destroy();
        chartRef.current = null;
      }
    };
  }, [data]);

  return <canvas ref={canvasRef}></canvas>;
};

// Bar Chart Component - FIXED
const BarChart = ({ data }) => {
  const canvasRef = useRef(null);
  const chartRef = useRef(null);

  useEffect(() => {
    if (!canvasRef.current) return;

    // Destroy existing chart before creating new one
    if (chartRef.current) {
      chartRef.current.destroy();
      chartRef.current = null;
    }

    const ctx = canvasRef.current.getContext('2d');
    
    try {
      chartRef.current = new Chart.Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true
            }
          },
          plugins: {
            legend: {
              position: 'bottom',
            }
          }
        }
      });
    } catch (error) {
      console.error('Error creating bar chart:', error);
    }

    // Cleanup function
    return () => {
      if (chartRef.current) {
        chartRef.current.destroy();
        chartRef.current = null;
      }
    };
  }, [data]);

  return <canvas ref={canvasRef}></canvas>;
};

// File Detail Component
const FileDetail = ({ fileData }) => {
  if (!fileData) {
    return (
      <div className="text-center text-gray-500 py-12">
        Select a file from the sidebar or upload a new one
      </div>
    );
  }

  const typeDistributionData = {
    labels: Object.keys(fileData.type_distribution || {}),
    datasets: [
      {
        label: 'Type Distribution',
        data: Object.values(fileData.type_distribution || {}),
        backgroundColor: [
          '#FF6384',
          '#36A2EB',
          '#FFCE56',
          '#4BC0C0',
          '#9966FF',
          '#FF9F40',
        ],
      },
    ],
  };

  const perTypeTypes = Object.keys(fileData.per_type_stats || {});
  const perTypeFlowrate = perTypeTypes.map(type => fileData.per_type_stats[type].avg_flowrate);
  const perTypePressure = perTypeTypes.map(type => fileData.per_type_stats[type].avg_pressure);
  const perTypeTemperature = perTypeTypes.map(type => fileData.per_type_stats[type].avg_temperature);

  const perTypeBarData = {
    labels: perTypeTypes,
    datasets: [
      {
        label: 'Avg Flowrate',
        data: perTypeFlowrate,
        backgroundColor: '#3B82F6',
      },
      {
        label: 'Avg Pressure',
        data: perTypePressure,
        backgroundColor: '#10B981',
      },
      {
        label: 'Avg Temperature',
        data: perTypeTemperature,
        backgroundColor: '#F59E0B',
      },
    ],
  };

  return (
    <div>
      {/* Overall Stats */}
      <div className="bg-white p-6 rounded-lg shadow-lg mb-6">
        <h3 className="text-2xl font-bold mb-4 text-gray-800">Overall Statistics</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="bg-blue-50 p-4 rounded">
            <div className="text-sm text-gray-600">Total Records</div>
            <div className="text-2xl font-bold text-blue-600">{fileData.total_records}</div>
          </div>
          <div className="bg-green-50 p-4 rounded">
            <div className="text-sm text-gray-600">Avg Flowrate</div>
            <div className="text-2xl font-bold text-green-600">{fileData.avg_flowrate?.toFixed(2)}</div>
          </div>
          <div className="bg-yellow-50 p-4 rounded">
            <div className="text-sm text-gray-600">Avg Pressure</div>
            <div className="text-2xl font-bold text-yellow-600">{fileData.avg_pressure?.toFixed(2)}</div>
          </div>
          <div className="bg-red-50 p-4 rounded">
            <div className="text-sm text-gray-600">Avg Temperature</div>
            <div className="text-2xl font-bold text-red-600">{fileData.avg_temperature?.toFixed(2)}</div>
          </div>
        </div>
      </div>

      {/* Type Distribution Chart */}
      <div className="bg-white p-6 rounded-lg shadow-lg mb-6">
        <h3 className="text-2xl font-bold mb-4 text-gray-800">Type Distribution</h3>
        <div className="h-96">
          <PieChart data={typeDistributionData} />
        </div>
      </div>

      {/* Per Type Stats Table */}
      <div className="bg-white p-6 rounded-lg shadow-lg mb-6">
        <h3 className="text-2xl font-bold mb-4 text-gray-800">Per Type Statistics (Table)</h3>
        <div className="overflow-x-auto">
          <table className="min-w-full table-auto">
            <thead className="bg-gray-200">
              <tr>
                <th className="px-4 py-2 text-left">Type</th>
                <th className="px-4 py-2 text-left">Count</th>
                <th className="px-4 py-2 text-left">Avg Flowrate</th>
                <th className="px-4 py-2 text-left">Avg Pressure</th>
                <th className="px-4 py-2 text-left">Avg Temperature</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(fileData.per_type_stats || {}).map(([type, stats]) => (
                <tr key={type} className="border-b hover:bg-gray-50">
                  <td className="px-4 py-2 font-semibold">{type}</td>
                  <td className="px-4 py-2">{stats.count}</td>
                  <td className="px-4 py-2">{stats.avg_flowrate?.toFixed(2)}</td>
                  <td className="px-4 py-2">{stats.avg_pressure?.toFixed(2)}</td>
                  <td className="px-4 py-2">{stats.avg_temperature?.toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Per Type Stats Chart */}
      <div className="bg-white p-6 rounded-lg shadow-lg">
        <h3 className="text-2xl font-bold mb-4 text-gray-800">Per Type Statistics (Chart)</h3>
        <div className="h-96">
          <BarChart data={perTypeBarData} />
        </div>
      </div>
    </div>
  );
};

// Dashboard Component
const Dashboard = ({ initialUploads, onLogout }) => {
  const [uploads, setUploads] = useState(() => {
    // Try to load from localStorage first
    const saved = localStorage.getItem('uploads');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {
        return initialUploads || [];
      }
    }
    return initialUploads || [];
  });
  
  const [selectedFile, setSelectedFile] = useState(() => {
    // Try to load selected file from localStorage
    const saved = localStorage.getItem('selectedFile');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {
        return null;
      }
    }
    return null;
  });
  
  const [currentFileData, setCurrentFileData] = useState(() => {
    // Try to load current file data from localStorage
    const saved = localStorage.getItem('selectedFile');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {
        return null;
      }
    }
    return null;
  });

  // Save uploads to localStorage whenever they change
  useEffect(() => {
    if (uploads && uploads.length > 0) {
      localStorage.setItem('uploads', JSON.stringify(uploads));
    }
  }, [uploads]);

  // Save selected file to localStorage whenever it changes
  useEffect(() => {
    if (selectedFile) {
      localStorage.setItem('selectedFile', JSON.stringify(selectedFile));
    }
  }, [selectedFile]);

  useEffect(() => {
    if (initialUploads && initialUploads.length > 0) {
      const newUploads = initialUploads.slice(0, 5);
      setUploads(newUploads);
      localStorage.setItem('uploads', JSON.stringify(newUploads));
    }
  }, [initialUploads]);

  const handleSelectFile = (upload) => {
    setSelectedFile(upload);
    setCurrentFileData(upload);
  };

  const handleUploadSuccess = (response) => {
    const newUpload = {
      id: Date.now(),
      file_name: 'New Upload',
      total_records: response.overall_stats.total_records,
      avg_flowrate: response.overall_stats.avg_flowrate,
      avg_pressure: response.overall_stats.avg_pressure,
      avg_temperature: response.overall_stats.avg_temperature,
      type_distribution: response.overall_stats.type_distribution,
      per_type_stats: response.per_type_stats,
    };
    
    const updatedUploads = [newUpload, ...uploads.slice(0, 4)];
    setUploads(updatedUploads);
    setSelectedFile(newUpload);
    setCurrentFileData(newUpload);
    localStorage.setItem('uploads', JSON.stringify(updatedUploads));
    localStorage.setItem('selectedFile', JSON.stringify(newUpload));
  };

  const handleLogout = () => {
    // Clear all stored data on logout
    localStorage.removeItem('uploads');
    localStorage.removeItem('selectedFile');
    onLogout();
  };

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar 
        uploads={uploads} 
        selectedFile={selectedFile} 
        onSelectFile={handleSelectFile} 
      />
      <div className="flex-1 overflow-y-auto">
        <div className="bg-white shadow-sm p-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-800">Chemical Equipment Parameter Visualizer</h1>
          <button
            onClick={handleLogout}
            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
          >
            Logout
          </button>
        </div>
        <div className="p-6">
          <UploadCSV onUploadSuccess={handleUploadSuccess} />
          <FileDetail fileData={currentFileData} />
        </div>
      </div>
    </div>
  );
};

// Main App Component
function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [showRegister, setShowRegister] = useState(false);
  const [lastUploads, setLastUploads] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initializeApp = async () => {
      const token = localStorage.getItem('token');
      if (token) {
        try {
          // Verify token and fetch user uploads by attempting to access a protected endpoint
          // Since we don't have a dedicated /me endpoint, we'll just set authenticated
          // and let the dashboard handle empty uploads
          setIsAuthenticated(true);
          
          // You can add a call to fetch uploads here if your backend has an endpoint
          // For now, we'll just mark as authenticated
        } catch (error) {
          // Token is invalid, clear it
          localStorage.removeItem('token');
          setIsAuthenticated(false);
        }
      }
      setLoading(false);
    };

    initializeApp();
  }, []);

  const handleLogin = (data) => {
    setIsAuthenticated(true);
    setLastUploads(data.last_uploads || []);
  };

  const handleRegister = (data) => {
    setIsAuthenticated(true);
    setLastUploads([]);
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setIsAuthenticated(false);
    setLastUploads([]);
    setShowRegister(false);
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="text-center">
          <div className="text-xl font-semibold text-gray-700">Loading...</div>
          <div className="mt-2 text-sm text-gray-500">Please wait</div>
        </div>
      </div>
    );
  }

  if (!isAuthenticated) {
    if (showRegister) {
      return (
        <Register
          onRegister={handleRegister}
          onSwitchToLogin={() => setShowRegister(false)}
        />
      );
    }
    return (
      <Login
        onLogin={handleLogin}
        onSwitchToRegister={() => setShowRegister(true)}
      />
    );
  }

  return <Dashboard initialUploads={lastUploads} onLogout={handleLogout} />;
}

export default App;