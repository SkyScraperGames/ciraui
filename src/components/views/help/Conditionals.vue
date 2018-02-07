<template>
  <div class="container content">
    <h1>Python - Conditionals</h1>

    <p>
      Conditionals, also known as conditional statements and if/else statements are a very important part of programming because
      they allow the programs you write to make decisions.
    </p>

    <p>
      Conditional statements are just code that tells the computer to do something&nbsp;
      <strong>if</strong> a certain condition is true. An example of a conditional in real life would be:
    </p>

    <p style="text-align: center;">
      <em>If it is raining outside, I will bring an umbrella.</em>
    </p>
    <p>
      This conditional says that you will bring an umbrella with you if it is raining. It is then implied that if it is not raining,
      you will not bring the umbrella. The same goes for conditionals in programming. If the condition is met, then the code
      within will execute. If it is not, the computer will move on.</p>
    In Python, conditionals&nbsp;are basically a series of
    <router-link to="/help/booleans">Boolean Statements</router-link> paired with the keywords if:, elif:, and else:. A group of conditionals is called a conditional
    block. They are always initiated with an if statement such as:
    <p></p>

    <pre><code>if x &lt; 8:
      print "The value of x is less than 8"</code></pre>

    <p>
      In this example,&nbsp;
      <strong>if</strong> the value that x is holding&nbsp;
      <strong>is less than</strong> 8, the code within the if statement will execute. Otherwise, nothing will happen. This is because
      if statements execute&nbsp;
      <strong>if&nbsp;</strong>the boolean statement inside them evaluates to True.
    </p>

    <p>
      In addition to the if statement, there are two other types of statements that can be part of a conditional block. First of
      these is the else statement. Continuing the example above, an else statement that might go with the if statement that
      was given earlier would be:
    </p>

    <pre><code>else:
      print "The value of x is greater than 8"</code></pre>

    <p>
      Else statements like this one execute when the if statement or the elif statement (covered below) that comes before them
      does not. In this case, the else statement would execute if the boolean statement&nbsp;
      <em>x &lt; 8&nbsp;</em>evaluates to False.
    </p>

    <p>
      The last type of conditional statement in Python is the elif statement. This is a sort of hybrid of the if and else statements.
      It must always follow an if statement or another elif statement, and if the statement before an elif statement does not
      execute, the computer tests a&nbsp;boolean statement within the elif, and executes the elif's code if it evaluates to
      True. If it evaluates to False, the computer moves on. Continuing with the example from above, an elif statement might
      look like:
    </p>

    <pre><code>elif x == 8:
      print "The value of x is 8"</code></pre>

    <p>
      Using if, elif, and else statements, you can create a complete conditional block. Not every block has to use each type of
      statement. Some use only if statements, some use an if and an else, and some use all 3. It is important to note that
      though you normally only use one if statement and one else statement, one conditional block can contain many elif statements.
    </p>
  </div>
</template>
