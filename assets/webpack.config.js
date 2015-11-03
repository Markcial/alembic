module.exports = {
    entry: "./js/entry.jsx",
    output: {
        path: __dirname,
        filename: "bundle.js"
    },
    devtool: 'inline-source-map',
    module: {
        loaders: [
            { test: /\.css$/, loader: "style!css" },
            {
              test: /\.jsx$/,
              loader: 'babel',
              exclude: /node_modules/, query: {
                presets: ["es2015", "react"]
              }
            },
        ]
    }
};
