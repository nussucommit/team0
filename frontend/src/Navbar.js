const Navbar = () => {

    const registerPage = () => {
        console.log('redirecting to register page');
    }

    const loginPage = () => {
        console.log('redirecting to login page');
    }
    
    return (
        <nav className="navbar">
            <h1>Team0Blog</h1>
            <div className="links">
                <button block size="lg" type="submit" onClick={() => registerPage()}>
                Register
                </button>
                <button block size="lg" type="submit" onClick={() => loginPage()}>
                Login
                </button>

            </div>
        </nav>
    );
}
 
export default Navbar;
