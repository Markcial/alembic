import React from 'react';
import ReactDOM from 'react-dom';
import {CommentBox, SearchBar} from './Graphics.jsx';

const Mui = require('material-ui');

let injectTapEventPlugin = require("react-tap-event-plugin");

//Needed for onTouchTap
//Can go away when react 1.0 release
//Check this repo:
//https://github.com/zilverline/react-tap-event-plugin
injectTapEventPlugin();

class Application extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        results: props.results
    };
  }

  onResultsFound (response) {
    var foundResults = [];
    response.data.albums.items.forEach((album) => {
      if (album.images.length) {
        album.picture = album.images[0].url;
      }
      foundResults.push(album);
    })
    this.setState({results:foundResults});
  }

  render() {
    return (<div>
      <SearchBar onResultsFound={this.onResultsFound.bind(this)} />
      <div>
        {this.state.results.map(result =>

        <Mui.Card initiallyExpanded={false}>
          <Mui.CardHeader
            title={result.name}
            subtitle="Subtitle"
            avatar={<Mui.Avatar>A</Mui.Avatar>}
            actAsExpander={true}
            showExpandableButton={true}
              />
          <Mui.CardMedia expandable={true} overlay={<Mui.CardTitle title={result.name} subtitle=""/>}>
            <img src={result.picture}/>
          </Mui.CardMedia>
        </Mui.Card>
          )}
      </div>
      <CommentBox />
      </div>
    )
  }
}
Application.propTypes = {results: React.PropTypes.array};
Application.defaultProps = { results:[]};

var app = document.getElementById('application');
ReactDOM.render(<Application />, app);
