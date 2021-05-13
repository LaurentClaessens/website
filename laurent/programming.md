# My programming page

You can find my realisations and their documentation on my <a href="https://github.com/LaurentClaessens">github account</a>.

## Python, Sage
   

### phystricks

The module [phystricks](https://github.com/LaurentClaessens/phystricks) is a Python2 module using Sage. It serves to generate  [tikz](http://paws.wcu.edu/tsfoguel/tikzpgfmanual.pdf) code ready to be included in you LaTeX document.

This module allows you to create arbitrarily complex pictures using python and Sage and include them in LaTeX; all the math is performed by Sage and LaTeX is left with only points and segments. You are thus not restricted by the LaTeX's internal limitation about programming and computations. 

The point is that you do not have to know anything about Tikz or any programming/drawing from the LaTeX side. 

* The project on [github](https://github.com/LaurentClaessens/phystricks)
* [Some demonstrative pictures](pdf/phystricks-demo.pdf) (not all of them are impressive, but they are there for testing/demonstration purposes)
* [The user manual](pdf/phystricks-doc.pdf)
* [The code documentation](phystricks/doc/html/index.html).


## C++


### finitediff
   

The program  `finitediff` will be an implementation of the finite difference method for solving differential equations. It is also my sandbox for experiment the numerical methods that I studied.

Content:

* Implement the PLU decomposition
* start implementing the conjugated gradient method

See also: 

* [The projet on github](https://github.com/LaurentClaessens/finitediff)
* [The code documentation](finitediff/doc/html/index.html)


<h3>lora</h3>

<p><a href="https://github.com/LaurentClaessens/lora">lora</a> is my backup program. It synchronizes a backup of your home directory while keeping a copy of modified and removed files. Thus you never loose data. It is written in C++.</p>
<p></p>
<p><a href="https://github.com/LaurentClaessens/lora">Sources and documentation on github</a></p>

<h3>gitme</h3>

<p><a href="https://github.com/LaurentClaessens/gitme">gitme</a> recursively parses you home directory and avises you when a git repository needs a "git commit" or an update of the ".gitignore".</p>

<p><a href="https://github.com/LaurentClaessens/gitme">Sources and documentation on github</a></p>

<h2>Java</h2>

<h3>actors</h3>

<a href="https://github.com/LaurentClaessens/actors">actors</a> is a generic actor system written in Java with as a Maven project for the course of <a href="https://github.com/rcardin/pcd-actors">concurrent and distributed computing</a> at the Padua university.

<p><a href="https://github.com/LaurentClaessens/actors">Sources and documentation on github</a></p>

<h3>frtex</h3>

<p>
<a href="https://github.com/LaurentClaessens/frtex">frtex</a> is an implementation of the previous actor system. The aim is to recursively replace all <code>\input</code> in a LaTeX document by its content. frtex provides a class <code>LatexCode</code> with a method <code>getExplicitCode</code> that returns the answer as a <code>String</code>. The actor system is created under the hood, while the end user only deals with his <code>LatexCode</code> instance.
</p>

<p><a href="https://github.com/LaurentClaessens/frtex">Sources and documentation on github</a></p>

## PHP

As an exercice, I am writing my [my blog in PHP](http://laurent.claessens-donadello.eu/blog/php/intro.php). All the sources are [on github](https://github.com/LaurentClaessens/phpBlog).

   </body>
</html>

