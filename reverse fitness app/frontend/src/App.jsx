import { useState } from "react";
import "./App.css";

function App() {
  const [activeTab, setActiveTab] = useState("Home");
  const [water, setWater] = useState(1750);

  const waterGoal = 2500;
  const waterPercent = Math.min((water / waterGoal) * 100, 100);

  const tabs = [
    ["⌂", "Home"],
    ["▥", "Progress"],
    ["▣", "Food"],
    ["✦", "AI Coach"],
    ["♙", "Profile"],
  ];

  return (
    <div className="app">

      {/* HEADER */}
      <header className="topbar">
        <h1>▰ Reverse Fitness</h1>

        <div className="streak">
          🔥 4 Days
        </div>

        <div className="header-icons">
          <button>↗</button>
          <button>♙</button>
        </div>
      </header>


      {/* MAIN CONTENT */}
      <main className="content">

        {/* HOME */}
        {activeTab === "Home" && (
          <>
            <section className="welcome-card">

              <p>DAILY BALANCE • SAT, AUG 22</p>

              <h2>Good day, Alex! 👋</h2>

              <p className="quote">
                “True health is not about extreme strain —
                it's about listening to your body and finding
                daily balance.”
              </p>

              <div className="stats">
                <span>🔥 4 Day Streak</span>
                <span>✓ 4 Days Completed</span>
              </div>

            </section>


            {/* METRICS TITLE */}
            <div className="metrics-title">
              <h2>Today's Balance Metrics</h2>
              <span>Balanced Goal vs Hard Rules</span>
            </div>


            {/* METRIC CARDS */}
            <div className="grid">

              {/* SLEEP */}
              <div className="card sleep-card">

                <div className="metric-icon sleep-icon">
                  🌙
                </div>

                <h3>Sleep</h3>

                <strong>8.5 <small>hrs</small></strong>

                <p>Sleep Duration</p>

                <div className="progress">
                  <div
                    className="progress-fill sleep-progress"
                    style={{ width: "85%" }}
                  ></div>
                </div>

              </div>


              {/* WATER */}
              <div className="card water-card">

                <div className="metric-icon water-icon">
                  💧
                </div>

                <h3>Hydration</h3>

                <strong>
                  {water}
                  <small> / {waterGoal} ml</small>
                </strong>

                <button
                  className="add-water"
                  onClick={() =>
                    setWater(Math.min(water + 250, waterGoal))
                  }
                >
                  +
                </button>

                <div className="progress">
                  <div
                    className="progress-fill water-progress"
                    style={{ width: `${waterPercent}%` }}
                  ></div>
                </div>

              </div>


              {/* ACTIVITY */}
              <div className="card activity-card">

                <div className="metric-icon activity-icon">
                  ❤️
                </div>

                <h3>Activity</h3>

                <strong>
                  50 <small>min</small>
                </strong>

                <p>Active Time</p>

                <div className="progress">
                  <div
                    className="progress-fill activity-progress"
                    style={{ width: "80%" }}
                  ></div>
                </div>

              </div>


              {/* SENSOR */}
              <div className="card sensor-card">

                <div className="sensor-top">

                  <div className="metric-icon sensor-icon">
                    👟
                  </div>

                  <span className="sensor-status">
                    SENSOR ON
                  </span>

                </div>

                <h3>Steps</h3>

                <strong>0</strong>

                <p>Sensor Ready</p>

                <div className="progress">
                  <div
                    className="progress-fill sensor-progress"
                    style={{ width: "10%" }}
                  ></div>
                </div>

              </div>

            </div>
          </>
        )}


        {/* PROGRESS */}
        {activeTab === "Progress" && (
          <section>

            <h2>📊 Progress</h2>

            <div className="card">
              <h3>🔥 Current Streak</h3>
              <strong>4 Days</strong>
              <p>Keep maintaining your healthy routine.</p>
            </div>

            <div className="card">
              <h3>🏆 Badges Earned</h3>

              <p>🌱 First Step</p>
              <p>💧 Hydration Hero</p>
              <p>🌟 Perfect Balance</p>
            </div>

          </section>
        )}


        {/* FOOD */}
        {activeTab === "Food" && (
          <section>

            <h2>🍎 Food</h2>

            <div className="card">

              <h3>Food Analysis</h3>

              <p>
                Upload a food photo to analyze your meal.
              </p>

              <input
                type="file"
                accept="image/*"
              />

            </div>

          </section>
        )}


        {/* AI COACH */}
        {activeTab === "AI Coach" && (
          <section>

            <h2>✨ AI Coach</h2>

            <div className="card">

              <h3>Your Personal Coach</h3>

              <p>
                Your goal is balance, not extreme routines.
              </p>

              <input
                type="text"
                placeholder="Ask your AI coach..."
              />

              <button className="coach-button">
                Send
              </button>

            </div>

          </section>
        )}


        {/* PROFILE */}
        {activeTab === "Profile" && (
          <section>

            <h2>👤 User Profile</h2>

            <div className="profile-card">

              <div className="avatar">
                A
              </div>

              <h2>Alex</h2>

              <p>Age 26 • Reverse Fitness Balanced Member</p>

              <div className="card">

                <h3>⚙ Personal Information & Daily Targets</h3>

                <p>Target Sleep: 8 hours</p>
                <p>Target Water: 2500 ml</p>
                <p>Active Minutes Goal: 30</p>
                <p>Rest Break: 45 mins</p>

              </div>

            </div>

          </section>
        )}

      </main>


      {/* BOTTOM NAVIGATION */}
      <nav className="bottom-nav">

        {tabs.map(([icon, name]) => (

          <button
            key={name}
            className={activeTab === name ? "active" : ""}
            onClick={() => setActiveTab(name)}
          >

            <span className="nav-icon">
              {icon}
            </span>

            <span>
              {name}
            </span>

          </button>

        ))}

      </nav>

    </div>
  );
}

export default App;