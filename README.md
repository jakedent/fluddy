<div align="center">
  <img src="art/fluddy.png" width="250" height="250" alt="pytube logo" />
  <p align="center">
	  <img src="https://img.shields.io/badge/python-3.5%2B-blue" />
	  <img src="https://img.shields.io/badge/pypi-0.0.3-blue" />
	 <img src="https://img.shields.io/badge/downloads-154%2F%20month-brightgreen" />
	  <img src="https://img.shields.io/badge/Compatibility-MacOS.%20Windows.%20Linux.-lightgrey" />
	  
	  
	 
  </p>
  
</div>


# fluddy (dep)

*fluddy* is an effective, lightweight and dependency-free command-line utility for managing, launching, updating and creating Flask Apps.


<!-- ABOUT THE PROJECT -->
## Description


       __ _           _     _
      / _| |         | |   | |
     | |_| |_   _  __| | __| |_   _
     |  _| | | | |/ _` |/ _` | | | |
     | | | | |_| | (_| | (_| | |_| |
     |_| |_|\__,_|\__,_|\__,_|\__, |
                               __/ |
      Version: 0.0.3          |___/


Flask is fast becoming the most popular web development framework for Python. Developers will typically manage multiple Flask apps individually where each app will rely on its own virtual environment - this can become time consuming when launching and updating multiple Flask Apps in development. 

Flask Buddy (fluddy) allows developers to launch and update their individual Flask Apps through a simple Command-Line Interface. CLI functionality also allows developers to create a launchable 'Hello from Fluddy' Flask App and to add previously created Flask Apps to fluddy for painless launches and updates.

### Built With

* [Python 3.5]()


<!-- GETTING STARTED -->
## Installation

* Download fluddy repo.
* Change to fluddy dir.
* Run the following command:

```
pip install .
```

<!-- USAGE EXAMPLES -->
## Usage
Add a Flask App to fluddy: 

```
fluddy --add projectName /exact/path/to/app/dir
```

Launch a Flask App:

```
fluddy projectName
```
Create a Flask App:

```
fluddy --create projectName /exact/path/to/save/dir
```
Create a Flask App from template / skeleton (coming v0.0.4):

```
fluddy --create-skel projectName /exact/path/to/save/dir /exact/path/to/template/skeleton
```
Update a Flask App (venv):

```
fluddy --update projectName
```
Remove a Flask App from fluddy:

```
fluddy --remove projectName
```


<div align="center">
<br>
 <img src="art/fluddy-demo-min-2.gif" alt="pytube logo" />
</div>
<!-- ROADMAP -->

## Issues

See [open issues](https://github.com/jakedent/fluddy/issues) for a proposed list of features (and 🐞's).



<!-- CONTRIBUTING -->
## Contributing

Contributions **welcomed and appreciated** under the categories:

1. General Improvements.
2. Optimisation of code.
3. Optimisation of structure.
3. Recommendations.
4. Additional features.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jacob Dent - info@jacobdent.com

[https://github.com/jakedent/fluddy](https://github.com/jakedent/fluddy)

[https://pypi.org/project/fluddy/](https://pypi.org/project/fluddy/)

