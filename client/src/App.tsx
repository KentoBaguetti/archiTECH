import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 to-gray-800 flex flex-col items-center justify-center text-white">
      <button className="border p-4" onClick={() => setCount(count + 1)}>
        Count {count}
      </button>
    </div>
  );
}

export default App;
