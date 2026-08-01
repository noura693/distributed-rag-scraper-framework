import { useState } from "react";

function App() {
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);

  const search = async () => {
    const response = await fetch(
      `http://127.0.0.1:8000/search?query=${searchQuery}`
    );

    const data = await response.json();

    setSearchResults(data);
  };

  const askRag = async () => {
    const response = await fetch(
      `http://127.0.0.1:8000/rag?question=${question}`
    );

    const data = await response.json();

    setAnswer(data.answer);
    setSources(data.sources);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Distributed RAG Scraper Framework</h1>

      <hr />

      <h2>Semantic Search</h2>

      <input
        type="text"
        placeholder="Search..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />

      <button onClick={search}>Search</button>

      <div>
        {searchResults.map((item, index) => (
          <p key={index}>{item.text}</p>
        ))}
      </div>

      <hr />

      <h2>RAG Question Answering</h2>

      <input
        type="text"
        placeholder="Ask a question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askRag}>Ask</button>

      <h3>Answer</h3>
      <p>{answer}</p>

      <h3>Sources</h3>

      <ul>
        {sources.map((source, index) => (
          <li key={index}>{source}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;