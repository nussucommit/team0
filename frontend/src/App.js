import Navbar from './Navbar';
import Home from './Home';
import Create from './Create';
import NotFound from './NotFound';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import BlogDetails from './BlogDetails';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar /> {/*self-closing tag, not within switch component, always show*/}
        <div className="content">
          <Switch> {/* ensures only one route component shows up at any one time */}
            <Route exact path="/"> 
              <Home />
            </Route>
            <Route exact path="/create">
              <Create /> {/* looks from top to bottom, so stops at path */}
            </Route>
            <Route path="/blogs/:id"> 
              <BlogDetails />
            </Route>
            <Route path="*">
              <NotFound />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App; // so that it can be used else where
