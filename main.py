import os
import json


def main():
    root = 'D:/Users/User/FrontendProjects'
    project_name = input('Enter project name: ').strip()

    os.chdir(root)
    os.system(f'mkdir {project_name}')
    os.chdir(f'{root}/{project_name}')
    os.system('npm init -y')
    print('Installing necessary libraries.....')
    os.system('npm i --save-dev webpack webpack-cli webpack-dev-server sass css-loader html-webpack-plugin '
              'mini-css-extract-plugin ts-loader typescript @types/react @types/react-dom  sass-loader style-loader')
    os.system('npm i react react-dom')

    with open('.gitignore', 'w') as f:
        f.write('/node_modules\n/coverage\n/build\n.DS_Store\n.env\nnpm-debug.log\nFooter')

    with open('declaration.d.ts', 'w') as f:
        f.write('declare module \'*.scss\';')

    with open('tsconfig.json', 'w') as f:
        f.write('{\n  \"compilerOptions\": {\n    \"esModuleInterop\": true,\n    \"jsx\": \"react\",'
                '\n    \"module\": \"esnext\",\n    \"moduleResolution\": \"node\",\n    \"lib\": [\n      \"dom\",'
                '\n      \"esnext\"\n    ],\n    \"strict\": true,\n    \"sourceMap\": true,\n    \"target\": '
                '\"esnext\",\n  },\n  \"exclude\": [\n    \"node_modules\"\n  ]\n}')

    with open('webpack.config.js', 'w') as f:
        f.write('const prod = process.env.NODE_ENV === \'production\';\n\nconst HtmlWebpackPlugin = require('
                '\'html-webpack-plugin\');\nconst MiniCssExtractPlugin = require('
                '\'mini-css-extract-plugin\');\n\nmodule.exports = {\n  mode: prod ? \'production\' : '
                '\'development\',\n  entry: \'./src/index.tsx\',\n  output: {\n    path: __dirname + \'/dist/\','
                '\n  },\n  module: {\n    rules: [\n      {\n        test: /\\.(ts|tsx)$/,\n        exclude: '
                '/node_modules/,\n        resolve: {\n          extensions: [\'.ts\', \'.tsx\', \'.js\', \'.json\'],'
                '\n        },\n        use: \'ts-loader\',\n      },\n      {\n        test:  /\\.s[ac]ss$/i,'
                '\n        use: [\n          // Creates `style` nodes from JS strings\n          \"style-loader\",'
                '\n          // Translates CSS into CommonJS\n          \"css-loader\",\n          // Compiles Sass '
                'to CSS\n          \"sass-loader\"\n        ],\n      },\n    ]\n  },\n  devtool: prod ? undefined : '
                '\'source-map\',\n  plugins: [\n    new HtmlWebpackPlugin({\n      template: \'index.html\',\n    }),'
                '\n    new MiniCssExtractPlugin(),\n  ],\n};')

    filename = 'package.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        data['scripts']['start'] = 'webpack serve --port 3000'
        data['scripts']['build'] = 'NODE_ENV=production webpack'

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    with open('index.html', 'w') as f:
        f.write(
            '<!DOCTYPE html>\n<html>\n<head lang=\"en\">\n  <title>Hello React</title>\n</html>\n<body>\n  <div '
            'id=\"app-root\">App is loading...</div>\n</body>')

    os.system(f'mkdir src')
    os.chdir(f'{root}/{project_name}/src')

    with open('index.tsx', 'w') as f:
        f.write(
            'import React from \'react\'\nimport { createRoot } from \'react-dom/client\'\nimport App from '
            '\'./components/App\'\n\nconst container = document.getElementById(\'app-root\')!\nconst root = '
            'createRoot(container)\nroot.render(<App/>)')

    os.system(f'mkdir components')
    os.chdir(f'{root}/{project_name}/src/components')
    os.system(f'mkdir App')
    os.chdir(f'{root}/{project_name}/src/components/App')

    with open('index.tsx', 'w') as f:
        f.write(
            'import React from \"react\";\nimport style from \'./App.module.scss\'\n\nconst App: React.FC = () => {\n '
            '   return   (\n    <h1 className={style.test}>Hello React!</h1>\n    )\n    \n}\n\nexport default App;')

    with open('App.module.scss', 'w') as f:
        f.write(
            '.test {\n    text-align: center;\n}')

    print('Script done.')


if __name__ == '__main__':
    main()
