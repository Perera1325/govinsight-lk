import React, { useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import "chart.js/auto";

function App() {
  const [form, setForm] = useState({
    household_id: 1,
    monthly_income: "",
    family_size: "",
    housing_condition: 1,
    sanitation: 0,
    education_access: 0,
    health_risk: 0
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: Number(e.target.value)
    });
  };

  const analyze = async () => {
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/poverty/analyze",
        form
      );
      setResult(res.data);
    } catch (err) {
      alert("Error connecting to backend");
    }
  };

  const chartData = result
    ? {
        labels: ["Poverty Score"],
        datasets: [
          {
            label: "Score",
            data: [result.poverty_score]
          }
        ]
      }
    : null;

  return (
    <div style={{ padding: 40 }}>
      <h1>EquiLanka Poverty Analysis</h1>

      <input
        name="monthly_income"
        placeholder="Monthly Income"
        onChange={handleChange}
      />
      <br />

      <input
        name="family_size"
        placeholder="Family Size"
        onChange={handleChange}
      />
      <br />

      <label>Housing Condition</label>
      <select name="housing_condition" onChange={handleChange}>
        <option value={1}>Poor</option>
        <option value={2}>Average</option>
        <option value={3}>Good</option>
      </select>
      <br />

      <label>Sanitation</label>
      <select name="sanitation" onChange={handleChange}>
        <option value={0}>No Toilet</option>
        <option value={1}>Basic</option>
        <option value={2}>Good</option>
      </select>
      <br />

      <label>Education Access</label>
      <select name="education_access" onChange={handleChange}>
        <option value={0}>Poor</option>
        <option value={1}>Average</option>
        <option value={2}>Good</option>
      </select>
      <br />

      <label>Health Risk</label>
      <select name="health_risk" onChange={handleChange}>
        <option value={0}>Low</option>
        <option value={1}>Medium</option>
        <option value={2}>High</option>
      </select>
      <br /><br />

      <button onClick={analyze}>Analyze Household</button>

      {result && (
        <div>
          <h2>Result</h2>
          <p>Poverty Score: {result.poverty_score}</p>
          <p>Level: {result.poverty_level}</p>

          <h3>Recommendations</h3>
          <ul>
            {result.recommendations.map((rec, i) => (
              <li key={i}>{rec}</li>
            ))}
          </ul>

          <div style={{ width: 400 }}>
            <Bar data={chartData} />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;