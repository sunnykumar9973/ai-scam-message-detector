/**
 * ResultCard Component
 * Displays prediction results with:
 * - Prediction (Safe/Scam)
 * - Confidence percentage
 * - Probability breakdown
 * - Algorithm info
 */

import React from 'react';

function ResultCard({ result }) {
  const { prediction, confidence, probability, algorithm, is_scam } = result;

  // Color based on prediction
  const bgColor = is_scam ? 'bg-red-500/20 border-red-500/50' : 'bg-green-500/20 border-green-500/50';
  const textColor = is_scam ? 'text-red-400' : 'text-green-400';
  const accentColor = is_scam ? 'bg-red-600' : 'bg-green-600';

  return (
    <div className={`space-y-6 p-6 rounded-xl border ${bgColor}`}>
      
      {/* Main Prediction */}
      <div className="text-center">
        <div className={`inline-block px-6 py-3 rounded-lg ${accentColor} text-white font-bold text-2xl`}>
          {prediction}
        </div>
      </div>

      {/* Confidence */}
      <div className="bg-white/5 rounded-lg p-4 border border-white/10">
        <div className="flex items-center justify-between mb-2">
          <span className="text-gray-300 font-medium">Confidence</span>
          <span className={`text-2xl font-bold ${textColor}`}>{confidence}%</span>
        </div>
        {/* Progress bar */}
        <div className="w-full bg-gray-700 rounded-full h-2">
          <div
            className={`${accentColor} h-2 rounded-full transition-all duration-500`}
            style={{ width: `${confidence}%` }}
          ></div>
        </div>
      </div>

      {/* Probability Breakdown */}
      <div className="space-y-3">
        <p className="text-gray-300 font-medium">Probability Distribution:</p>
        
        {/* Safe Probability */}
        <div className="space-y-1">
          <div className="flex justify-between text-sm">
            <span className="text-gray-400">✅ Safe (Ham)</span>
            <span className="text-green-400 font-semibold">{probability.safe}%</span>
          </div>
          <div className="w-full bg-gray-700 rounded-full h-2">
            <div
              className="bg-green-500 h-2 rounded-full transition-all duration-500"
              style={{ width: `${probability.safe}%` }}
            ></div>
          </div>
        </div>

        {/* Scam Probability */}
        <div className="space-y-1">
          <div className="flex justify-between text-sm">
            <span className="text-gray-400">🚨 Scam (Spam)</span>
            <span className="text-red-400 font-semibold">{probability.scam}%</span>
          </div>
          <div className="w-full bg-gray-700 rounded-full h-2">
            <div
              className="bg-red-500 h-2 rounded-full transition-all duration-500"
              style={{ width: `${probability.scam}%` }}
            ></div>
          </div>
        </div>
      </div>

      {/* Algorithm Info */}
      <div className="bg-blue-500/10 border border-blue-500/30 rounded-lg p-3">
        <p className="text-blue-300 text-sm">
          <span className="font-semibold">Algorithm:</span> {algorithm}
        </p>
        <p className="text-blue-300 text-xs mt-1">
          Uses TF-IDF vectorization to convert text into numerical features and Logistic Regression to classify messages.
        </p>
      </div>
    </div>
  );
}

export default ResultCard;
