# codingame-python-merger

<!--- For more shields, check https://shields.io --->
![GitHub repo size](https://img.shields.io/github/repo-size/ejulia/codingame-python-merger?style=flat)
![GitHub contributors](https://img.shields.io/github/contributors/ejulia/codingame-python-merger)
![GitHub](https://img.shields.io/github/license/ejulia/codingame-python-merger)
![GitHub stars](https://img.shields.io/github/stars/ejulia/codingame-python-merger?style=social)
![GitHub forks](https://img.shields.io/github/forks/ejulia/codingame-python-merger?label=Fork&style=social)

codingame-python-merger is a tool that allows the [Codingame](https://www.codingame.com/home) players to organize their Python code into multiple files. It is best used with the [Codingame Sync app and extension](https://www.codingame.com/forum/t/codingame-sync-beta/614) to push automatically your code to the plateform's editor.

During the Codingame AI competitions, the bot code can become quite big for a single file. This project lets you organize your Python code into multiple files, and automatically merge these into a single file that you can either copy or push to the Codingame online editor.

Have fun!


## Prerequesites

Before you begin, ensure that Python 2+ is installed and running on your machine.


## Installing codingame-python-merger

* Just clone this project on your computer, and start coding your bot!
* If you want to use the [Codingame Sync App](https://www.codingame.com/forum/t/codingame-sync-beta/614), the file to sync with is **merge.py** (not *merger.py*).


## Using codingame-python-merger

* Only the code written in the main/ directory will be appended to the merge.py file.
* In the main/ directory, you can organize your code in as many sub-directories as you wish.
* Only the *\*.py* files will be merged, links (either symbolic or real) and files with another or no extension will be ignored.
* The **main.py** file is appended last to the **merge.py** file, hence that is where your main code should be written.
* When you are ready, execute the **merger.py** script. It will automatically merge all the appropriate files in the **merge.py** file. Library imports are managed during the process. If you are using the [Codingame Sync App](https://www.codingame.com/forum/t/codingame-sync-beta/614), your code should be automatically pushed to the Codingame online editor once when the merge is complete.

* If you want to unit-test your code, use the **test/** directory. The code there won't be appended to the merge.py file.


## Contributing to codingame-python-merger

To contribute to codingame-python-merger, please refer to the GitHub documentation on [creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

## Contributors

* [@ejulia](https://github.com/ejulia) 💻 📖


## Contact

If you want to contact me you can reach me at emmanuel.julia@ik.me.


## License

This project is licensed under the Open Source MIT License - see the [LICENSE](https://github.com/ejulia/codingame-python-merger/blob/main/LICENSE) file for details.


## Acknowledgments

This README.md file was written using [scottydocs' README-template.md](https://github.com/scottydocs/README-template.md), the [all-contributors emoji key](https://allcontributors.org/docs/en/emoji-key), and shields from [shields.io](https://shields.io/).
