import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const search = async () => {
    const response = await fetch(
      `http://127.0.0.1:8000/search?query=${query}`
    );

    const data = await response.json();

    setResults(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Distributed RAG Scraper</h1>

      <input
        type="text"
        placeholder="Search..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={search}>
        Search
      </button>

      <hr />

      {results.map((item, index) => (
        <div key={index}>
          <p>{item.text}</p>
        </div>
      ))}
    </div>
  );
}

export default App;