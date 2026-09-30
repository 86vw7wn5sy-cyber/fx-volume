import React, { useEffect, useState } from 'react';
import './styles.css';

const API_URL = 'http://localhost:8000/api/v1';

function App() {
  const [pairs, setPairs] = useState([]);
  const [selectedPair, setSelectedPair] = useState('EURUSD');
  const [market, setMarket] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API_URL}/market/pairs`)
      .then((res) => res.json())
      .then((data) => {
        setPairs(data.pairs);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  useEffect(() => {
    if (!selectedPair) return;
    fetch(`${API_URL}/market/${selectedPair}`)
      .then((res) => res.json())
      .then((data) => setMarket(data))
      .catch(() => setMarket(null));
  }, [selectedPair]);

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <h1>FX Volume</h1>
        <p>AI Forex Analysis</p>
        <div className="pair-list">
          {pairs.map((pair) => (
            <button
              key={pair}
              className={pair === selectedPair ? 'pair active' : 'pair'}
              onClick={() => setSelectedPair(pair)}
            >
              {pair}
            </button>
          ))}
        </div>
      </aside>

      <main className="content">
        <header className="topbar">
          <div>
            <span className="badge">Forex Intelligence</span>
            <h2>{selectedPair}</h2>
          </div>
        </header>

        {loading ? (
          <div className="loading">Loading market...</div>
        ) : market ? (
          <>
            <section className="metrics-grid">
              <div className="card price-card">
                <label>Current Price</label>
                <strong>{market.price}</strong>
              </div>
              <div className="card">
                <label>Change</label>
                <strong>{market.change_percent}%</strong>
              </div>
              <div className="card">
                <label>Volume</label>
                <strong>{market.volume}</strong>
              </div>
              <div className="card">
                <label>Trend</label>
                <strong>{market.trend}</strong>
              </div>
            </section>

            <section className="analysis-grid">
              <div className="card panel">
                <h3>Trade Signal</h3>
                <p>{market.signals.trend}</p>
                <p>RSI: {market.signals.rsi}</p>
                <p>Volume: {market.signals.volume_strength}</p>
                <p>Momentum: {market.signals.momentum}</p>
              </div>

              <div className="card panel">
                <h3>Risk</h3>
                <p>Level: {market.risk.risk_level}</p>
                <p>Stop loss: {market.risk.stop_loss}</p>
                <p>Take profit: {market.risk.take_profit}</p>
              </div>
            </section>
          </>
        ) : (
          <div className="loading">Unable to load data.</div>
        )}
      </main>
    </div>
  );
}

export default App;
