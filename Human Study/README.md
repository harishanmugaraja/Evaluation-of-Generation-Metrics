# Human Study

This folder contains the code related to the human study.

## Get Started

### Dependencies
Start by installing required dependencies:
You will need Node.js and Python3 to run this project.

[Node.js](https://nodejs.org/en/download/)

[Python3](https://www.python.org/downloads/)

From this folder, run:
```sh
npm install
```
```sh
pip install Flask
```
```sh
cd api/image_server
npm install
```
### Get images
The images themselves are are on fid00.umiacs.umd.edu.
Use your favorite client to copy the images folder into ./public.
If you are not an author and would like access to the images, please contact the authors of the study.

## Run Frontend
### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## Run Flask server
```sh
./api/runapp.sh
```
OR
```sh
cd api/
flask run
```

## Run Image Server
```sh
cd api/image_server
node app.js
```

