import { Link } from 'react-router-dom';

const Navbar = () => {
    return ( 
        <nav className="navbar">
            <h1>Team 0</h1>
            <div className="links">
                {/* <a href="/">Home</a> */}
                <Link to="/">Home</Link>
                <Link to="/create" style={{
                    color: "white",
                    backgroundColor: '#f1356d',
                    borderRadius: '8px',
                }}>New Blog</Link> {/** first curly brace means dynamic value, inner one for js obeject */}
                <Link to='/login'>Logout</Link>
            </div>
        </nav>
    );
}
 
export default Navbar;