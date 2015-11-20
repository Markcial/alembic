import React from 'react';
import axios from 'axios';

const Mui = require('material-ui');

export class SearchBar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        value: props.value,
        total: 0
    };
    this.apiEndpoint = 'https://api.spotify.com/v1/search';
  }

  search (event) {
    axios.get(this.apiEndpoint, {
      params: {
        q: this.state.value,
        type: 'album'
      }
    })
    .then(this.props.onResultsFound)
    .catch(this.props.onRequestError);

    return false;
  }

  handleChange (event) {
    this.setState({value: event.target.value});
  }

  render () {
    return <form action="" method="">
      <Mui.TextField value={this.state.value} onChange={this.handleChange.bind(this)} hintText="Search term" name="q" />
      <Mui.FlatButton label="Search" onClick={this.search.bind(this)} />
    </form>
  }
}
SearchBar.propTypes = {
  value: React.PropTypes.any,
  onResultsFound: React.PropTypes.func.isRequired,
  onRequestError: React.PropTypes.func
};
SearchBar.defaultProps = { value: "Hello!", onRequestError: function (response){}};

export class CommentBox extends React.Component {
  render() {
    return <div className="commentBox">
    Hello, world! I am a CommentBox.
    </div>
  }
}
