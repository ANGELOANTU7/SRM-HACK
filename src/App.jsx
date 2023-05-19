
import {BrowserRouter, Routes, Route} from "react-router-dom"
import Home from "./components/Home"
import UploadNotes from "./components/UploadNotes";
import RecordNotes from "./components/RecordNotes";

function App() {
  return (
    <div className="container">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/uploadnotes" element={<UploadNotes/>} />
          <Route path="/recordnotes" element={<RecordNotes/>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;