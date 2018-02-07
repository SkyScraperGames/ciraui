<template>
  <div class="container content">
    <h1>Python - Whitespace</h1>

    <p>
      When programming in Python, you need to include something called “whitespace” in order for the computer to understand what
      you are telling it to do. Whitespace is like punctuation.
    </p>

    <p>
      For example, if I wrote:
    </p>
    <p style="text-align: center;">
      <em>“I can’t wait to see my friends, Mom and Dad.” </em>
    </p>
    <p>
      my reader might not understand what I am saying. They might think my Mom and Dad are the friends I can’t wait to see. To
      avoid this, I can add punctuation to clarify what I am saying to my reader:
    </p>
    <p style="text-align: center;">
      <em>“I can’t wait to see my friends, Mom, and Dad.” </em>
    </p>

    <p>
      The same goes for code. All programming languages have “punctuation.” Computers need things in a particular order to understand
      our ideas, because they don’t speak our language . In Python, this is done through blank space.
    </p>

    <p>
      Whitespace can be created by using the tab button:
    </p>

    <img src="../../../assets/tab.jpg" alt="tab" width="130" height="82">

    <p>
      Here is an example of code with proper whitespace:
    </p>
    <pre><code>def update(self):
      if cira.keys.getKey("1-Left"):
          self.R = 255
          self.G = 0
          self.B = 0
    </code></pre>

    <p>
      Here is an example of the same code missing whitespace. Can you figure out what the errors are?
    </p>

    <pre><code>def update(self):
    if cira.keys.getKey("1-Left"):
          self.R = 255 self.G = 0
      self.B = 0
    </code></pre>

    <p>
      To fix this code, you would hit the tab button once at the start of the “if” line and the “self.B”, and you would need to
      hit the enter (return) button to put “self.G = 0” onto its own line.
    </p>

    <p>
      In Python, indents are used to mark code that belongs inside of a bigger piece of code. For example, we indent code that
      goes inside a class, function, conditional statement, or loop.
    </p>

    <p>
      Here’s an example using conditional statements:
    </p>

    <pre><code>if playerHealth &lt; 0:
    print ‘Oh no! Game Over!’
    </code></pre>

    <p>
      The line that says “print ‘Oh no! Game Over!’” must be indented with tab because it is a part of the larger if-statement
      on the line before it. If you did not put in the whitespace, the program would get confused and output an error message.
    </p>

    <p>
      A good way to tell if you need to tab in is to check if there is a colon (:) at the end of a line. When there’s a colon,
      there needs to be at least one line after it that is tabbed in.
    </p>
  </div>
</template>
