/**
 * Main App Component
 * Scam Message Detector - Frontend
 * 
 * Core Features:
 * - Text input for SMS messages
 * - API call to Flask backend
 * - Display prediction results
 * - Show confidence and probabilities
 * - Loading state management
 * - Error handling
 */

import React, { useState } from 'react';
import axios from 'axios';
import ResultCard from './components/ResultCard';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // API endpoint - adjust if backend runs on different port
  const API_ENDPOINT = 'http://localhost:5000/predict';

  /**
   * Handle "Detect Scam" button click
   * 1. Validate input
   * 2. Send message to backend
   * 3. Receive prediction
   * 4. Display result
   */
  const handleDetect = async (e) => {
    e.preventDefault();
    
    // Validation
    if (!message.trim()) {
      setError('Please enter a message to analyze');
      setResult(null);
      return;
    }

    if (message.length > 5000) {
      setError('Message is too long (max 5000 characters)');
      setResult(null);
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      // Send message to backend
      const response = await axios.post(API_ENDPOINT, {
        message: message
      });

      // Display result
      setResult(response.data);
      setError('');

    } catch (err) {
      // Handle errors
      if (err.response?.data?.error) {
        setError(err.response.data.error);
      } else if (err.message === 'Network Error') {
        setError('Cannot connect to server. Is Flask backend running on port 5000?');
      } else {
        setError('An error occurred. Please try again.');
      }
      setResult(null);
    } finally {
      setLoading(false);
    }
  };

  /**
   * Clear all inputs and results
   */
  const handleReset = () => {
    setMessage('');
    setResult(null);
    setError('');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 px-4 py-12">
      {/* Background accent */}
      <div className="fixed inset-0 pointer-events-none">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-blue-500 rounded-full mix-blend-multiply filter blur-3xl opacity-10 animate-blob"></div>
        <div className="absolute -bottom-8 right-1/4 w-96 h-96 bg-purple-500 rounded-full mix-blend-multiply filter blur-3xl opacity-10 animate-blob animation-delay-2000"></div>
      </div>

      <div className="max-w-2xl mx-auto relative z-10">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="inline-block mb-4">
            <span className="text-5xl">🛡️</span>
          </div>
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 leading-tight">
            Smart Scam Detector
          </h1>
          <p className="text-lg text-gray-300 max-w-md mx-auto">
            AI-Powered SMS Security Analysis
          </p>
          <p className="text-sm text-gray-400 mt-3">
            Using Logistic Regression & TF-IDF Technology
          </p>
        </div>

        {/* Main Card */}
        <div className="bg-white/5 backdrop-blur-lg border border-white/10 rounded-2xl p-8 shadow-2xl">
          
          {/* Form */}
          <form onSubmit={handleDetect} className="space-y-6">
            {/* Input Area */}
            <div>
              <label htmlFor="message" className="block text-sm font-medium text-gray-300 mb-3">
                Paste your message here:
              </label>
              <textarea
                id="message"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Enter an SMS message to check if it's a scam or safe..."
                disabled={loading}
                className="w-full h-32 px-4 py-3 rounded-lg border border-gray-600 bg-gray-800/50 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none transition disabled:opacity-50"
              />
              <div className="mt-2 text-sm text-gray-400">
                {message.length}/5000 characters
              </div>
            </div>

            {/* Error Message */}
            {error && (
              <div className="p-4 bg-red-500/10 border border-red-500/50 rounded-lg">
                <p className="text-red-400 text-sm">⚠️ {error}</p>
              </div>
            )}

            {/* Buttons */}
            <div className="flex gap-4">
              <button
                type="submit"
                disabled={loading}
                className="flex-1 px-6 py-3 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-semibold rounded-lg transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
              >
                {loading ? (
                  <>
                    <span className="inline-block animate-spin">⏳</span>
                    Analyzing...
                  </>
                ) : (
                  <>
                    🔍 Detect Scam
                  </>
                )}
              </button>
              
              <button
                type="button"
                onClick={handleReset}
                disabled={loading}
                className="px-6 py-3 bg-gray-700 hover:bg-gray-600 text-white font-semibold rounded-lg transition disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Clear
              </button>
            </div>
          </form>

          {/* Result Display */}
          {result && (
            <div className="mt-8 pt-8 border-t border-gray-600">
              <ResultCard result={result} />
            </div>
          )}
        </div>

        {/* Info Footer */}
        <div className="mt-8 text-center text-sm text-gray-400">
          <p>This model is trained on real SMS spam data using Machine Learning techniques.</p>
        </div>
      </div>
    </div>
  );
}

export default App;
