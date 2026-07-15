'use client';

import { useState } from 'react';

export default function Home() {
  const [loading, setLoading] = useState(false);
  const [predictedPrice, setPredictedPrice] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  const [formData, setFormData] = useState({
    OverallQual: 6,
    OverallCond: 5,
    YearBuilt: 1990,
    LotArea: 10000,
    '1stFlrSF': 1200,
    '2ndFlrSF': 0,
    TotalBsmtSF: 1000,
    FullBath: 2,
    HalfBath: 0,
    GarageCars: 2
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: Number(value) }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPredictedPrice(null);

    try {
      const response = await fetch('http://127.0.0.1:5001/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (data.success) {
        setPredictedPrice(data.predicted_price);
      } else {
        setError(data.error || 'Failed to predict price');
      }
    } catch (err) {
      setError('Failed to connect to the prediction server. Make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div className="header">
        <h1>House Price Predictor</h1>
        <p>AI-Powered Real Estate Valuation</p>
      </div>

      <div className="glass-panel">
        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            <div className="input-group">
              <label>Overall Quality (1-10)</label>
              <input type="number" min="1" max="10" name="OverallQual" value={formData.OverallQual} onChange={handleChange} required />
            </div>
            
            <div className="input-group">
              <label>Overall Condition (1-10)</label>
              <input type="number" min="1" max="10" name="OverallCond" value={formData.OverallCond} onChange={handleChange} required />
            </div>

            <div className="input-group">
              <label>Year Built</label>
              <input type="number" min="1800" max="2026" name="YearBuilt" value={formData.YearBuilt} onChange={handleChange} required />
            </div>

            <div className="input-group">
              <label>Lot Area (sqft)</label>
              <input type="number" name="LotArea" value={formData.LotArea} onChange={handleChange} required />
            </div>

            <div className="input-group">
              <label>1st Floor Area (sqft)</label>
              <input type="number" name="1stFlrSF" value={formData['1stFlrSF']} onChange={handleChange} required />
            </div>

            <div className="input-group">
              <label>2nd Floor Area (sqft)</label>
              <input type="number" name="2ndFlrSF" value={formData['2ndFlrSF']} onChange={handleChange} required />
            </div>

            <div className="input-group">
              <label>Basement Area (sqft)</label>
              <input type="number" name="TotalBsmtSF" value={formData.TotalBsmtSF} onChange={handleChange} required />
            </div>

            <div className="input-group">
              <label>Full Bathrooms</label>
              <input type="number" min="0" max="10" name="FullBath" value={formData.FullBath} onChange={handleChange} required />
            </div>

            <div className="input-group">
              <label>Half Bathrooms</label>
              <input type="number" min="0" max="10" name="HalfBath" value={formData.HalfBath} onChange={handleChange} required />
            </div>

            <div className="input-group">
              <label>Garage Cars</label>
              <input type="number" min="0" max="10" name="GarageCars" value={formData.GarageCars} onChange={handleChange} required />
            </div>
          </div>

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? <span className="spinner"></span> : 'Predict Value'}
          </button>
        </form>

        {predictedPrice !== null && (
          <div className="result-card">
            <h2>Estimated Home Value</h2>
            <div className="price">
              ${predictedPrice.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
            </div>
          </div>
        )}

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}
      </div>
    </div>
  );
}
