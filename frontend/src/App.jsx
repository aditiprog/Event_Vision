import { useEffect, useState } from "react";
import "./App.css";

function App() {

  const [data, setData] = useState({
    status: "Loading",
    spikes: 0,
    saved: 0
  });


  useEffect(() => {

    const interval = setInterval(() => {

      fetch("http://127.0.0.1:8000/metrics")
        .then(response => response.json())
        .then(result => {
          setData(result);
        })
        .catch(error => {
          console.log(error);
        });

    }, 1000);


    return () => clearInterval(interval);

  }, []);



  return (

    <div className="container">

      <h1>EventVision Dashboard</h1>

      <p>
        Event-Driven Neuromorphic Video Analytics
      </p>


      <div className="card">

        <h2>Status</h2>
        <h1>{data.status}</h1>

      </div>


      <div className="card">

        <h2>Spike Events</h2>
        <h1>{data.spikes}</h1>

      </div>


      <div className="card">

        <h2>Data Saved</h2>
        <h1>{data.saved}%</h1>

      </div>


    </div>

  );

}

export default App;