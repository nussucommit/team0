import Navbar from "./Navbar";
import Home from "./Home";
import Create from "./Create";
import NotFound from "./NotFound";
import Login from "./Login";
import SignUp from "./SignUp";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import BlogDetails from "./BlogDetails";
import Comment from "./Comment";
import { useState, useEffect } from "react";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const login = () => {
    setIsLoggedIn(localStorage.getItem("token"));
  };

  const logout = () => {
    setIsLoggedIn(false);
  };

  useEffect(() => {
    setIsLoggedIn(localStorage.getItem("token"));
  }, []);

  return (
    <Router>
      <div className="App">
        <Navbar isLoggedIn={isLoggedIn} logout={logout} />{" "}
        {/*self-closing tag, not within switch component, always show*/}
        <div className="content">
          <Switch>
            {" "}
            {/* ensures only one route component shows up at any one time */}
            <Route exact path="/">
              <Home />
            </Route>
            <Route exact path="/create">
              <Create /> {/* looks from top to bottom, so stops at path */}
            </Route>
            <Route path="/blogs/:id">
              <BlogDetails />
              <hr />
              <Comment />
            </Route>
            <Route path="/login">
              <Login login={login} />
            </Route>
            <Route path="/signup">
              <SignUp />
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
