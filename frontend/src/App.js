import Login from './containers/Login';
import Navbar from './Navbar';
function App() {

  const title = 'Team0-blog'

  return (
    <div className="App">
      <Navbar />
      <div className="content">
        <Login></Login>
      </div>  
    </div>
  );
}

export default App;
