# tinywebcode

tinywebcode starter project.

---
## Table of Contents
- [tinywebcode](#tinywebcode)
  - [Table of Contents](#table-of-contents)
  - [Hypothesis](#hypothesis)
  - [Project Structure](#project-structure)
  - [Methodology](#methodology)
    - [Non-existant viable feature](#non-existant-viable-feature)
    - [Existing viable feature](#existing-viable-feature)
  - [Complexity](#complexity)
    - [Non-existant bloat](#non-existant-bloat)
    - [Existing bloat](#existing-bloat)
    - [References](#references)
  - [Contributing](#contributing)
    - [Reach Out!](#reach-out)

---
## Hypothesis
**tinywebcode** was a personal project to:
* host lots of half-baked tiny webapps for as cheaply as possible

---
## Project Structure
     tinywebcode/                                 <-- Root of your project
       |- .dockerignore                           <-- Docker ignore file
       |- .gitignore                              <-- Git ignore file
       |- README.md                               <-- This README markdown file
       +- fastchart/                              <-- Holds any files for Fastchart API

---
## Methodology

This is the minimum viable product (MVP) to test the above hypothesis.

### Non-existant viable feature
* host lots of half-baked tiny webapps for as cheaply as possible

### Existing viable feature

* free deploy runner: GitHub Action
* free tier serverless host: Netlify, Vercel
* free tier containerized serverless host: Google Cloud Run (GCR) (Crai2020_2)
* paid server host: DigitalOcean, GoDaddy

---
## Complexity

Count the cost of complexity, i.e. incremental reward and risk reduction, before evolving MVP.

### Non-existant bloat
* free tier deploy runner: Octopus Deploy
* free static host: GitHub Pages, Surge (Crai2020)
* free tier static host: Hostman
* free tier dynamic webapp host: Heroku, Glitch (Crai2020), Uffizzi
* paid serverless host (FAAS): AWS Lambda, Azure, Google Cloud Function (GCF) (Crai2020)

### Existing bloat 
* Nil

---
### References
- (Crai2020) Paul Craig, 13-Nov-2020, [Google Cloud Run: the best hosting platform for dynamic apps](https://dev.to/pcraig3/google-cloud-run-the-best-host-platform-for-dynamic-apps-4ma6)
- (Crai2020_2) Paul Craig, 13-Nov-2020, [Quickstart: Continuous deployment to Google Cloud Run using Github Actions](https://dev.to/pcraig3/quickstart-continuous-deployment-to-google-cloud-run-using-github-actions-fna)
- (Pien2020) R.I.Pienaar, accessed 14-Nov-2020, [Free for Dev](https://github.com/ripienaar/free-for-dev)

---
## Contributing

Please read the [contributing guide](https://github.com/dennislwm/tinywebcode/blob/master/CONTRIBUTING.md) on how you can actively participate in the development of this repository.

---
### Reach Out!

Please consider giving this repository a star on GitHub.

```
16tinywebcode
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ config
│  ├─ description
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ master
│  │     └─ remotes
│  │        └─ origin
│  │           └─ master
│  ├─ modules
│  │  └─ apiopen
│  │     ├─ config
│  │     ├─ description
│  │     ├─ HEAD
│  │     ├─ hooks
│  │     │  ├─ applypatch-msg.sample
│  │     │  ├─ commit-msg.sample
│  │     │  ├─ fsmonitor-watchman.sample
│  │     │  ├─ post-update.sample
│  │     │  ├─ pre-applypatch.sample
│  │     │  ├─ pre-commit.sample
│  │     │  ├─ pre-push.sample
│  │     │  ├─ pre-rebase.sample
│  │     │  ├─ pre-receive.sample
│  │     │  ├─ prepare-commit-msg.sample
│  │     │  └─ update.sample
│  │     ├─ index
│  │     ├─ info
│  │     │  └─ exclude
│  │     ├─ logs
│  │     │  ├─ HEAD
│  │     │  └─ refs
│  │     │     ├─ heads
│  │     │     │  └─ master
│  │     │     └─ remotes
│  │     │        └─ origin
│  │     │           └─ HEAD
│  │     ├─ objects
│  │     │  ├─ 5b
│  │     │  │  └─ ec3031112c1193a360518ada7f32131b13a1cf
│  │     │  ├─ 8d
│  │     │  │  └─ 2a06d743868f516b6dcb2dc4476da66c56de4a
│  │     │  ├─ c0
│  │     │  │  └─ d1a5090a371effed8cce1eecc1fa7569892e29
│  │     │  ├─ c5
│  │     │  │  └─ 068dcba2c4cbc73fc5b1dd93bcce6b200b17ba
│  │     │  ├─ ee
│  │     │  │  └─ 7a464103d91b31d60fd401ba279c6caeb91dd5
│  │     │  ├─ fe
│  │     │  │  └─ e1b7c12f2e487c7c5f6affe7167c111a4b985e
│  │     │  ├─ info
│  │     │  └─ pack
│  │     ├─ packed-refs
│  │     └─ refs
│  │        ├─ heads
│  │        │  └─ master
│  │        ├─ remotes
│  │        │  └─ origin
│  │        │     └─ HEAD
│  │        └─ tags
│  ├─ objects
│  │  ├─ 18
│  │  │  └─ 71e197ced804b0e79186098dcf17f982918b2b
│  │  ├─ 22
│  │  │  └─ 14b7f869e01e641e32ad86c9a29b063456aeee
│  │  ├─ 33
│  │  │  └─ 702e72bd8a2c279ea142d2b0432ee80839925a
│  │  ├─ 34
│  │  │  └─ b3756c41f3e38163df757a667f9a860db63fb9
│  │  ├─ 4c
│  │  │  └─ df951c8144e1ae9db5f89a82ecb07895ab43b4
│  │  ├─ 80
│  │  │  ├─ 3fd551a7eac77c5a5492d46300f3e7f9661354
│  │  │  └─ d41da58202ce47d265bc90d782358fefaec5eb
│  │  ├─ 85
│  │  │  └─ 03d8f40be5954f5baae017bba1eb3b16200b00
│  │  ├─ a2
│  │  │  └─ 29fa70c7378717c00e97d4b863d49922a2fe7b
│  │  ├─ a4
│  │  │  └─ 8551c56286ddab22fd7d1fc8488fe5d1e4396c
│  │  ├─ b0
│  │  │  └─ 9f208eb7241b793f2af33aa5dc7e87758e991c
│  │  ├─ b3
│  │  │  └─ 59f815b79102e47e928dcbf9d66e8a3c6d2b36
│  │  ├─ bc
│  │  │  └─ 0a2d231a82d2eaa2249be23d224e90e99540f2
│  │  ├─ c1
│  │  │  └─ 99dedb21a3a7a9a43fd9e254cc4afc94f74598
│  │  ├─ e6
│  │  │  ├─ 915bac9f5cfb201c3f09707b4382a56d17cefc
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ ea
│  │  │  └─ 7463a013a1425de4ac918cc852c1d8ca585d7f
│  │  ├─ f9
│  │  │  └─ 3451dd9d08cf43da66ffe917de0302e9aec07b
│  │  ├─ info
│  │  └─ pack
│  └─ refs
│     ├─ heads
│     │  └─ master
│     ├─ remotes
│     │  └─ origin
│     │     └─ master
│     └─ tags
├─ .gitignore
├─ fastchart
│  ├─ .dockerignore
│  ├─ api_0.1
│  │  ├─ main.py
│  │  └─ models.py
│  ├─ api_0.2
│  │  ├─ main.py
│  │  └─ models.py
│  ├─ app
│  │  └─ fastchart.py
│  ├─ Dockerfile
│  ├─ fastapi.sh
│  ├─ requirements.txt
│  └─ __pycache__
│     └─ main.cpython-37.pyc
└─ README.md

```