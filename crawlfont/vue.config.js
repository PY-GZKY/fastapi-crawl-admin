
module.exports = {
  outputDir: process.env.outputDir,
  lintOnSave: true,
  publicPath:  process.env.NODE_ENV === 'production'
    ? './'
    : '/',
  assetsDir: 'dist',
  devServer: {
    port: 8001,
    open: true, //配置自动启动浏览器
    proxy: {
      '/api': {

        target: 'http://127.0.0.1:8000', //对应自己的接口
        // target: 'http://10.10.11.208:8000/',- //对应自己的接口
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          '^/api': '/'
        }
      }
    }
  },

};

