import React, { Component } from 'react';

class Like extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicks: 0,
      show: true
    };
  }

  ToggleClick = () => {
    this.setState({ show: !this.state.show });
  }

  render() {
    return (
      <div className="">
        <button onClick={this.ToggleClick}>
          { this.state.show ? 'Like: 0' : 'Like: 1' }
        </button>
      </div>
    );
  }
}

export default Like;