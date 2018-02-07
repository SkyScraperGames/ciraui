<template>
  <div class="container content">
    <h1>Python - Booleans</h1>

    <p>
      Statements that can either be true or false are called “Boolean statements.” You have seen may have seen True or False questions
      before – these are also Booleans. An example would be “1 + 1 = 2, true or false?” Booleans are used in code as special
      types of variables that can only store the value true, or the value false.
    </p>

    <p>
      For example:
    </p>

    <pre><code>bool = 3 &lt; 5</code></pre>

    <p>
      “bool” is a Boolean – this variable can either be True or False. In this case, “bool” is true because 3 is less than 5. The
      variable “bool” would be set to the value “True.” But, if I replaced 3 with 8, the statement would now be:
    </p>

    <pre><code>bool = 8 &lt; 5</code></pre>

    <p>
      The variable “bool” would be set to False in this case, because 8 is greater than, not less than, 5.
    </p>

    <hr>

    <p>
      Booleans can also be found in “conditional statements” and “loops.” They are useful when you want the program to perform
      differently depending on whether something is true or false.
    </p>

    <p>
      For example:
    </p>

    <pre><code>if playerScore &gt; 10:
      print ‘You win!’ </code></pre>

    <p>
      Here, the variable playerScore is holding the number of points which the player has earned in the game. As long as playerScore
      is less than ten, this condition will be false, so nothing will happen. But, as soon as the player gets more than 10
      points, the statement will be true, and the program will run the line of code after the colon (:) This statement prints
      “You win!” because the player has earned more than 10 points.
    </p>

    <p>
      These statements use inequalities to compare whether a Boolean is true or false. In math, you use =, &lt; and &gt; to make
      these comparisons. In coding, inequalities look like this:
    </p>

    <ul>
      <li>&lt; ("less than")</li>
      <li>&gt; ("greater than")</li>
      <li>&lt;= ("less than or equal to")</li>
      <li>&gt;= ("greater than or equal to")</li>
      <li>== ("equal to")</li>
      <li>!= ("not equal to")</li>
    </ul>

    <p>
      Notice that code uses “==” instead of “=” to compare whether two numbers are equal to one another! So instead of saying 2
      = 2, you would write 2 == 2 in Python.
    </p>
  </div>
</template>
