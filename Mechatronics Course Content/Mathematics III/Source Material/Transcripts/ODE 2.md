# ODE Lecture Transcript 2

> [!info] Source navigation
> [[Mathematical Modelling and Numerical ODEs|Related concept]] · [[Mathematics III Roadmap|Course roadmap]] · [[Mathematics III Overview|Subject overview]]

- And so, um. Oh. So let's start the course and then our why notes on the screen.
    
    0:02
    
- So you can, um. Yeah. Uh, follow this the notes quite easily.
    
    0:12
    
- Hopefully. So the first one, the lecture one. Um, so each week we will cover about three lectures.
    
    0:17
    
- Um, so for the first lectures, um, we introduce our course.
    
    0:24
    
- Um, the course is about mostly about modelling.
    
    0:29
    
- So, uh, what's modelling is that we try to use these mathematical models to describe a physical process or a, um, physical phenomenon.
    
    0:32
    
- Right. And then the models. Um, we are trying to find some solutions for the models.
    
    0:42
    
- We try to solve that, uh, mathematically.
    
    0:48
    
- And then also with from the answers, we try to interpret what the solution means physically.
    
    0:52
    
- So that's the process. Um, so the modelling part is sometime is quite a it's not an exact science.
    
    0:58
    
- Um, so you need to make some assumptions and then you need to, um, adjust sometimes and then.
    
    1:05
    
- So there's no actually correct models. So um, because every models you need to make some assumptions and the assumptions may not be always accurate.
    
    1:13
    
- But um, even though the model may not be correct, but it can be useful.
    
    1:23
    
- Um, so so that's why we need to spend some time to understand these models, how to build these models and how to, um, find solutions to these models.
    
    1:28
    
- So the aim is to translate the physical problems into, um, mathematical formulations or mathematical, um, language.
    
    1:38
    
- Um, in particular, in this course we are going to um, models a physical, um, phenomenon using mostly differential equations.
    
    1:52
    
- Yeah. And that will be the focus, um, in this paper. All right.
    
    2:02
    
- Um, so the, um.
    
    2:13
    
- Yeah, the focus of our paper is that we are trying to build a mathematical models using differential equations to describe a physical, um, problems.
    
    2:16
    
- And then we try to find solutions to these models and then understand what's going on,
    
    2:26
    
- um, in terms of the solutions and interpret the solutions physically.
    
    2:33
    
- So that's the um, yeah, that's the process of our papers.
    
    2:38
    
- Um, so let's just draw some diagram to illustrate, um, how we going to do that?
    
    2:43
    
- So suppose we have a physical problems or a physical systems we want to described.
    
    2:50
    
- And then um, so based on the discussions um,
    
    2:55
    
- we are going to have is that we are trying to use some mathematical models to describe these physical systems.
    
    2:58
    
- Right. So that's the first step is to try up or to make some assumptions to come up with a reasonable models to describe these physical systems.
    
    3:04
    
- So that's the first step. And then um we using some techniques in mathematics to find solutions to these uh, models, um, to find solutions.
    
    3:14
    
- And then we try to understand the solutions, um, by interpretations and understand the physical meanings for the solutions.
    
    3:25
    
- And then these interpretations help us to understand more about the original physical systems we want to, um, study.
    
    3:34
    
- So that's the process. And sometimes we need to repeat this process um, several times to get a better understanding.
    
    3:42
    
- Right. So we have to have physical systems. And then um, we want to use a models to describe these problems.
    
    3:49
    
- Um, yeah. By making some assumptions and find solutions to these problems in these steps.
    
    3:57
    
- And then from the solutions we found some physical interpretations, physical meanings for the solutions.
    
    4:03
    
- And that's how us to understand the systems better. All right.
    
    4:10
    
- So that's the diagrams for the process. Um, softmax cells.
    
    4:14
    
- All right. Um. Right.
    
    4:22
    
- Um. So let's go through, uh, some simple example to illustrate this point.
    
    4:26
    
- Uh, not going through the model itself, but how, uh, what we mean by a physical system and how do we do some, um, descriptions of these problems.
    
    4:30
    
- Right. So, for example, um, to consider that there's a ball dropping from a very tall building and then, um,
    
    4:40
    
- we want to understand the positions of the ball, um, at different time points as a function of time.
    
    4:50
    
- And then so this is the physical problems, right? And then somehow you are trying to watch these systems using a, um, mathematical models.
    
    4:58
    
- And then by solving these models, then we understand what's the positions of the ball, um, at different time point.
    
    5:09
    
- And that's the answers we are going to get. Um, so what's the positions of the ball at different time points as a function of time?
    
    5:18
    
- Right. So that's the um, one simple example about how do we use mathematical models to answer these kind of physical questions.
    
    5:26
    
- Right. So you just draw a ball from a very tall buildings and then use models to describe these problems and then find solutions and also,
    
    5:36
    
- um, understand um, the positions as a function of time.
    
    5:44
    
- So this is the um, um, one example.
    
    5:49
    
- All right. Um, another one is that. Suppose that you imagine stairs, a, um, persons jumping parachute from aeroplane.
    
    5:56
    
- Right. Um, they in the Queenstown and then obviously.
    
    6:05
    
- Um, yeah. The, the people will uh, increasing the velocity, the speed very fast.
    
    6:08
    
- And how do you understand the velocity of the, uh, yeah.
    
    6:15
    
- These parachutist, um, as a function of time.
    
    6:19
    
- Yeah. To make sure that it must be safe and so on, so forth.
    
    6:24
    
- So this is also can be, um, understand by using mathematical models and then from the solutions.
    
    6:28
    
- Um, yeah. Um, we understand the speeds of these, uh, persons to make sure that, um, this, uh, activity is still quite safe.
    
    6:35
    
- Right. Um, so once the parachute opens, obviously you have a quite big air resistance.
    
    6:46
    
- Um, and then. Yeah. And then the speed will drop.
    
    6:51
    
- And then to make sure that, um, the time of the opening is, um, suitable, otherwise you will be predicting injuries.
    
    6:55
    
- Right. So these kind of problems can also be understand by using, uh, mathematical models.
    
    7:02
    
- Yeah. Um, right. Um, but this one, um, is discussed in, uh, in the textbook.
    
    7:08
    
- Right.
    
    7:15
    
- Um, sorry, I forgot to mention that the textbooks, um, the textbook is actually, um, this one, if you go down to the, uh, end page of the the slides,
    
    7:15
    
- the this, the textbooks we are going to use quite extensively, uh, which is called the advanced engineering mathematics.
    
    7:26
    
- Um, and the book is available on online, um, on campus.
    
    7:33
    
- So if you go to the chemist page. Um, and then you go to the resource cost resource right on the doorstep.
    
    7:38
    
- Yeah. And then you can see that, um, so you can view this book online.
    
    7:58
    
- Um, so yeah, whenever you want to look at.
    
    8:03
    
- Yeah. Just you should log in. All right then.
    
    8:07
    
- Then you should have access to this book. You can read this book online.
    
    8:19
    
- All right. Okay. Okay, so maybe some people are using. So I don't have to.
    
    8:28
    
- So you have six copies and then. Yeah. Right?
    
    8:32
    
- Um, but that's the textbook we are going to use in this course. Um.
    
    8:40
    
- Yeah. And then in this example, um, you want to understand more, you can look at this textbook and in particular this part.
    
    8:48
    
- Um. Um, the question sets one point. You at question 15 and then there's more detailed description of these problems.
    
    8:54
    
- Right. Um, yeah. Write some other examples.
    
    9:00
    
- Um, suppose you want to understand the displacements of a, um.
    
    9:06
    
- A mass on a spring. So. So that something looks like this.
    
    9:12
    
- Um. Yes.
    
    9:16
    
- Right. So that slide, these pictures, um, suppose that there's a mouse attached to a spring,
    
    9:29
    
- and then if you pull out the mouse and then release and then the object will go back and forth.
    
    9:35
    
- Right. So you imagine you have a spring and then you pull out the objects.
    
    9:40
    
- Um, yeah. In some point. And then you release the object and the object will go back and forth.
    
    9:45
    
- Right? Um, yeah. I mean, yeah, back and forth.
    
    9:51
    
- Um, so the question is that if you want to understand the displacements of this mouse and on this spring, it's a function of time.
    
    9:53
    
- And we can also do that um, by using mathematical models.
    
    10:03
    
- Right. And this is one of the classic classical problems in physics.
    
    10:06
    
- And then we'll discuss, um, these problems in more details in the later lectures.
    
    10:11
    
- But um, so this is just some examples that, um, we can use mathematics to describe these kind of physical problems.
    
    10:16
    
- And then, um, by finding the solutions, um, we understand what's going on in underlying this physical, um, process.
    
    10:23
    
- Right. So um, so that makes sense. So that's what we are going to discuss, um, in this paper.
    
    10:32
    
- Right. And then there's many, many more examples. We can use mathematical, mathematical models to help us to understand.
    
    10:39
    
- Yeah. So this is a list of them. Um, you, uh, obviously in this paper, we don't have time to go through all these details,
    
    10:45
    
- and some of them may be interesting to you, uh, in the future.
    
    10:53
    
- A lot these, uh, electrical circuits, if you're coming from the electrical engineering departments.
    
    10:56
    
- Right. But I'll cover some of them.
    
    11:02
    
- And then, uh, but you can see that there's quite a wide range of applications that can be used, um, by, um, by modelling.
    
    11:04
    
- Right. So modelling has quite why applications in this, uh, physical science.
    
    11:13
    
- All right. So, um. Yeah. So hopefully, uh, by going through this course, then that can help you to understand more,
    
    11:19
    
- um, how we can use these mathematical tools to solve some of the engineering problems.
    
    11:27
    
- So that's the, um, yeah, that's the, uh, plans, um, for our paper.
    
    11:32
    
- Right? Uh, so, yeah, that's the brief introductions what we are going to discuss in this paper.
    
    11:39
    
- And, um, but before we can actually do the model things, we have need to, uh, lay some foundations in mathematics.
    
    11:45
    
- Um, so, yeah, in the first few weeks, we will also mainly discuss, um, mathematic mathematical knowledge.
    
    11:53
    
- And then we have some applications to real life examples.
    
    12:00
    
- But first part is due. We are going to discuss some theory about mathematics before we can apply them into the, uh, physical problems.
    
    12:04
    
- Right. Yeah. We will do that. Um, usually in the tutorial and the quizzes and the assignments.
    
    12:13
    
- But in the lectures you are more, uh, more on the, uh, theoretical part.
    
    12:18
    
- Right? Um, as I mentioned, the focus of this paper is that using differential equations to describe a physical systems.
    
    12:25
    
- Um, so firstly what's the differential equations? Um, so probably some of you have heard that before.
    
    12:34
    
- Uh, but let's um, just refresh the memory.
    
    12:40
    
- Right. So differential equations, um, is that equations that involve a differential directive right.
    
    12:44
    
- Differentiations. So whenever you have equations with uh directive and that's called differential equations.
    
    12:53
    
- So like this example. So this is equations. And then in this equations we have something like this.
    
    13:00
    
- Or why would it. So that's the differentials. So equations with differentials.
    
    13:07
    
- Um they are differential equations. So that's the definitions right.
    
    13:12
    
- So equate um. So differential equation is basically just equations.
    
    13:21
    
- But that's uh related to uh involving some of the differential derivative.
    
    13:25
    
- Right. If there's only, uh, one variables.
    
    13:33
    
- One independent variables. Um, this equations is called ordinary differential equations.
    
    13:36
    
- And usually we just call them Odes. Um, so that's the focus in the first half of the semester.
    
    13:41
    
- And then if there's a function with more than one variables like 2 or 3 variables, um, that's called partial differential equations.
    
    13:47
    
- And that will be discussed in more details in the second half of the semester.
    
    13:55
    
- Right. In the first half we mostly discuss the ordinary.
    
    14:00
    
- So equations with just a function with one variables.
    
    14:03
    
- Right. So this is like the examples um. So, uh, why in these examples, why is the dependent variables.
    
    14:08
    
- So in these examples, um, we use this letter Y to um denote the dependent variables and then the letter T to denote the independent variables.
    
    14:42
    
- And sometimes we can use x or use other uh letters.
    
    14:52
    
- So the letter itself the same matters.
    
    14:56
    
- But uh usually the, the one um in this numerator is the dependent variables like y and then the one on the leaf,
    
    14:58
    
- uh in the denominators are the independent variables. So we have divided it.
    
    15:07
    
- And sometimes we just use y dash. Um so y dash just, just means um, the first relative dui over t.
    
    15:11
    
- Right? Um, so I'm sure I've seen this one in the, um, engineering mathematic 1 or 2.
    
    15:24
    
- Right. So this y dash and divide. So this is the dependent.
    
    15:31
    
- Uh, yeah. Variable y, um, over the independent variable T.
    
    15:35
    
- Right. Um, in this case wise, just a functions of one variables.
    
    15:43
    
- Uh, usually we use your X to denote these independent variables.
    
    15:47
    
- Right. And then y double dash. That means the second derivative or the second differentiations of y.
    
    15:51
    
- Um so there's the same notations driver t or y dash.
    
    15:59
    
- So that's just a uh the same same meanings, just a different notations.
    
    16:03
    
- All right. So whenever you have equations with differentials that's called a differential equations.
    
    16:08
    
- And that's the um yeah. The two we are going to use um many in our course.
    
    16:14
    
- Right.
    
    16:22
    
- Um, and then so, uh, a bit more complicated, it is called a partial differential equations is that you have, uh, two or more independent variables.
    
    16:23
    
- Right. So for example, like these um. So in this case, um.
    
    16:33
    
- Uh, let's see, um, you in these examples, you use the dependent variables.
    
    16:39
    
- For example, um, in this case, example you is the, um, you know, the dependent variables and then all these others, um, x, y, z and t.
    
    17:08
    
- Um, yeah. So that's one uh, in the denominators.
    
    17:17
    
- They are the independent variables. Right.
    
    17:21
    
- So in this case, we have a, um, you is a function.
    
    17:25
    
- In this example you is a functions of g and u is function of x.
    
    17:28
    
- And then in this notation um that's the partial derivative um we call them w over dolce.
    
    17:33
    
- So this is um so yeah it's quite similar to D but are we call them.
    
    17:40
    
- You use a slightly different notation. That means that you have a more than dependent and uh, depend on more than one variables.
    
    17:46
    
- Right. So this is a U is a function of t. And then u is also a function of x.
    
    17:55
    
- And then that's the partial derivative with respect to t.
    
    17:59
    
- And that this the uh partial derivative with respect to x.
    
    18:02
    
- And this equations uh some of the classical um partial differential equations.
    
    18:06
    
- And then we will discuss some of them in more detail in the second half of the semester.
    
    18:11
    
- Right. So that the first one is called, uh, one dimensional wave equations to describe how wave is propagated in the,
    
    18:16
    
- um, yeah, in the, in the, in the m and then we have the equations.
    
    18:24
    
- That means that how these, uh, heat is going to transfer from one object to other objects, um, so and so forth.
    
    18:30
    
- So these are some of the classical, uh, partial differential equations, um, that will be discussed in more detail in the second half of the paper.
    
    18:37
    
- All right. Um, so we have, um. So, yeah, in this course we are focus on this, uh,
    
    18:48
    
- trimming tools we are going to use for modelling the ordinary differential equations and the partial differential equations.
    
    18:55
    
- In the first half we talk about more all of these. And then in the second half we talk about a piece in more details.
    
    19:03
    
- Right. And then, um. Avoid differential equations, um, and estimations that you set up the equations and models.
    
    19:11
    
- And then you try to find some solutions to these models.
    
    19:21
    
- So what we mean by solutions. So solutions to a differential equations that means is that is a function that will satisfy the equations.
    
    19:24
    
- That means that um that makes the equations equals for both sides.
    
    19:34
    
- Right. So that's the solutions. So uh so let's look at a simple example to illustrate what we mean by solutions.
    
    19:39
    
- So um you have suppose we have a differential equation states in this form x y dash is equal to two y.
    
    19:47
    
- Right. So suppose you have a differential equations. Um x times y is equal to y.
    
    20:12
    
- And then we want to um verify that.
    
    20:18
    
- Um so we are going to verify.
    
    20:22
    
- So what we're going to do is that we want to verify that this functions is the solutions to the differential equations.
    
    20:50
    
- Right. So how do we do that. Um so the definition is that a solution is um so a function is a solution to the differential equation.
    
    20:56
    
- If you satisfy the uh, the left hand side of the equation is equal to the right hand side of the equation.
    
    21:08
    
- So let's check that. So how do we check is that basically we substitute the y into the equation.
    
    21:14
    
- So the left hand side is equal to x times y dash. So what we do here is that we just put these solutions inside to verify whether it's true or not.
    
    21:55
    
- We inside these y positions. So now x times the differentiate of this function c x squared over x right.
    
    22:05
    
- Yeah. And then we differentiate these function c times x square.
    
    22:26
    
- We got two times x. And then so the result will be just choose c times x square.
    
    22:29
    
- And that's the left hand side of the equations right. Of.
    
    22:35
    
- Right. And then, um, then we again substitute you y into the right hand side position.
    
    23:08
    
- So the wild side is going to try. And then once I see those c times x squared that means that two times six square.
    
    23:14
    
- And then we can check that the left hand side is equal to the right hand side.
    
    23:21
    
- That means that the function's um y is equal to c x square is the solutions because it's satisfy that
    
    23:25
    
- if you substitute the y into the left hand side and the right hand side of the differential equations,
    
    23:32
    
- then makes the equations equal to each other, right.
    
    23:37
    
- And that's why, um, we say that these functions which are solutions.
    
    23:41
    
- Okay. Right? Yeah.
    
    23:49
    
- So, uh, so, so far, um, I mean, at this moment, we haven't thought about how to find a solution.
    
    23:53
    
- Uh, what we do is that we are, um, we have provide you solutions.
    
    23:59
    
- And then from from the provided solutions, we can substitute you into the equation to check whether it's that is the true solutions or not.
    
    24:03
    
- Right. So that's, uh, what we're doing. But, um, later on we'll talk about how do we actually find this form.
    
    24:12
    
- So this is not always given. And then if it's not events.
    
    24:18
    
- And how do we find this form. Right. So it's that's the next step.
    
    24:22
    
- But um, but the first example just to um, illustrate what we mean by solutions,
    
    24:26
    
- a solution that means that if you put that into the original differential equations,
    
    24:32
    
- the left side and the right hand side, they should match each other.
    
    24:37
    
- And that's um, what we mean by solutions. All right.
    
    24:40
    
- Yeah. Um, yeah. You can ask if any question just by probably raising your hand or something like that.
    
    24:49
    
- Yeah. Right.
    
    24:55
    
- If it's okay, then that's, um. Continue. Um, yes.
    
    24:58
    
- Similarly, we can also, um, show that this one is another solutions to the differential equations.
    
    25:04
    
- Um, so we have a differential equations. And then um this form y is equal to c times e to the power x is also a solutions.
    
    25:11
    
- Um so let's briefly go through that.
    
    25:21
    
- Right. So another example we verified y is equal to this function form c times e to the power x is the solutions to the differential equations.
    
    25:53
    
- So the same strategies to the left hand side. All right.
    
    26:04
    
- Um. So the same strategies that we just put this y functions into these, um, positions.
    
    26:38
    
- So that's the second derivative, right. So, um.
    
    26:45
    
- So just put this y is equal to c times e to the power x into the second derivative, the y double dash.
    
    26:52
    
- And then minus minus y. And also put that into the y positions.
    
    26:59
    
- And then we differentiate this function twice. So because these are exponential functions.
    
    27:04
    
- So we differentiate. Once we've got the same function c times e to the power x and then differentiate again we still get the same functions.
    
    27:09
    
- So that's why we have the second differentiation.
    
    27:18
    
- Um the functional form is still the same which is c to the power x.
    
    27:22
    
- Yeah. Um, so. So after we differentiations tries, um, these functions, do you get the same form?
    
    27:50
    
- Um, so C is just a constant. So constants is still there.
    
    27:57
    
- And then exponential functions of the differentiations do give us the same exponential functions.
    
    28:02
    
- And yeah. And then they are the same. So when you subtract um you got zero.
    
    28:08
    
- Um because the left hand side and y and z are the same.
    
    28:13
    
- And therefore uh, we verify um, this function form is a solutions.
    
    28:17
    
- All right? Yeah. So. If we make sense.
    
    28:26
    
- Um, yeah. So this is a very similar examples.
    
    28:37
    
- I will not go through the details, but um, the same strategies.
    
    28:40
    
- Um, suppose that you are given the solution form and then what you do is that you substitute you into the left hand side of the equations,
    
    28:44
    
- and then you substitute into, if there a y here to check with the left hand side and the wild side or equal or not.
    
    28:52
    
- If they are equal then this is a solution. If it's not, then it's not right.
    
    28:58
    
- It's not solutions. So yeah, just um, do it as exercise.
    
    29:03
    
- All right. Um, yeah. So, um, so there's some more exercise for you to practice.
    
    29:13
    
- Um, you have these functions, and then, um, you can show that these two state solutions to differential equations and for these two examples.
    
    29:18
    
- Um, so this exercise will discuss in more details in the uh tutorial time.
    
    29:28
    
- So that's um, you should to call quickly John problem solving.
    
    29:35
    
- But um, that's usually the um, tutorial time.
    
    29:38
    
- And then um, yeah, just a reminder is that, uh, once you get familiar of these materials, um, you can ready to do the first quiz, right?
    
    29:42
    
- So the first quiz will be based on the, um, the material for the first week.
    
    29:51
    
- The first week basically is just the first three lectures.
    
    29:57
    
- Lecture one two, three. Yeah. Um, yeah.
    
    30:00
    
- So the due dates. Um, yeah, it's I don't remember the exact date, but, uh, if you log on to the canvas, then you can see the two dates.
    
    30:04
    
- Um, so this quiz are part of the, uh, assessment.
    
    30:12
    
- So, um, yeah, just to make sure that you put your efforts to, uh, to to get the quiz correct.
    
    30:15
    
- Right? Um. Yep. Yeah.
    
    30:24
    
- So, um, so that's the, um,
    
    30:27
    
- the material of the first lectures is quite often it's quite straightforward is that we introduce what we mean via differential equations.
    
    30:29
    
- Um, and then these differential equations can be used to model um, the physical problems um,
    
    30:36
    
- which we're going to discuss in more details in the later lectures.
    
    30:43
    
- But the first step is just to lay the foundations of the, um, some mathematical techniques.
    
    30:46
    
- And that's the differential equations. And uh, in particular in this paper, in the first lectures we talk about what do we mean by solutions.
    
    30:52
    
- And then how do we check. Uh, this one is actually solutions by just substituting the solutions inside the left hand
    
    31:00
    
- side and the right hand side of the equation to check whether they are equal or not.
    
    31:08
    
- All right. Yeah. So that's the, uh, first lectures.
    
    31:13
    
- Um, let's discuss a bit more about a second that just, um, you take a small break.
    
    31:17
    
- What? All right.
    
    31:22
    
- Um hmm. So the second lectures is about, um, we start to talk about how do we use all to start to, uh, modelling some, um, physical problems.
    
    31:35
    
- Right. So simple physical problems. And how do we use ODI to do that?
    
    31:47
    
- So, um, in the first lecture, we all, um, you see that we can find solutions to in odes and then, uh.
    
    31:55
    
- But how? But we haven't discussed. Um, that's a solution.
    
    32:05
    
- But how do we find these functions? Right. Um, there there's some.
    
    32:09
    
- There are three main strategies. How do we find the functions?
    
    32:14
    
- Um, the first one is called analytic solutions. That means that we try to get the solution formed.
    
    32:17
    
- Exactly. So the first approach is called analytic form.
    
    32:23
    
- Um, the second one is that we are using numerical solutions.
    
    32:27
    
- So we try to using some software package to find the solutions numerically.
    
    32:31
    
- Right. So that's the second strategy. And then the third one is called a qualitative.
    
    32:36
    
- So um so the qualitative is not the exact solutions.
    
    32:42
    
- But that can tell us the um some of the features um of the solutions.
    
    32:46
    
- So that's a framing approach.
    
    32:52
    
- And um, so we discussed briefly, um, for different equations we need to use different approach either analytically, numerically or quantitatively.
    
    32:55
    
- All right. So actually we have, um.
    
    33:05
    
- We have some previous knowledge to solve differential equations.
    
    33:18
    
- And, um, one way to do that is that we just doing that by finding antiderivative and integrations.
    
    33:21
    
- So that's already uh can be considered as to finding a differential equations.
    
    33:28
    
- Right. So um for differential equations of this form um y dash is equal to a function of x.
    
    33:33
    
- And then we can find a solution for y by doing the uh by finding the antiderivative.
    
    33:41
    
- Right. So.
    
    33:47
    
- Right. So, um.
    
    34:32
    
- So in the engineering course, uh, one and two, we discussed this one quite often is that we can, um, find the antiderivative, um, of a function y.
    
    34:33
    
- Yeah. By doing the integrations. Right. So this is already, uh, um, some form of a different, um, yeah.
    
    34:44
    
- Differential equations. So example. But in this example we consider this differential equation in this form y dash.
    
    34:52
    
- Or we can write as d or d x is equal to two x square plus uh cosine of two x.
    
    35:29
    
- And then we want to find a solution that means that we want to find y by doing the integrations.
    
    35:37
    
- Right. So we can find the functions of Y by, uh, finding the antiderivative, um, and integrations of the right hand side.
    
    35:45
    
- Um, and then there's just some other basic techniques for finding the, um, and iterative.
    
    36:24
    
- So, um, this is power X square. And then and iterative will be the power increase by one.
    
    36:30
    
- So x square becomes x to the power three. And then divide by three.
    
    36:38
    
- And then there's a constant in first. So two thirds times x cube.
    
    36:42
    
- And then it's cosine functions. Um yeah. Um we can use the chain rule to find that um the antiderivative will be the sine functions.
    
    36:46
    
- Um solve two x over two and plus arbitrary constants.
    
    36:54
    
- So um so that's already a solutions.
    
    36:59
    
- Um so that's the solutions for the differential equations, which is the um solution we want to find is y is in this form right.
    
    37:01
    
- So this is the simple um differential equations.
    
    37:10
    
- Um, which means that we, we, we solving these um, differential equations by finding the end of the functions.
    
    37:13
    
- All right. So if the equation is straightforward, then we can um solve the equations in this form.
    
    37:28
    
- Yeah. And then there's some exercise, um, which is quite similar.
    
    37:47
    
- Um, I will just go through one and then you can, um, discuss or, uh.
    
    37:51
    
- Yeah. I mean, um, to practice this exercise during the tutorial time.
    
    37:57
    
- So let's go through the maybe the last one. Right.
    
    38:01
    
- You try to find. Why is he going to checks? Look, you're not going to.
    
    38:18
    
- All right. And then we can find that. Um, so first we find the we integrate integration one.
    
    38:40
    
- So the second derivative becomes the first true divide. So y is equal to the integration of the right hand side.
    
    38:45
    
- Um so two x. And then that gives us that x square.
    
    38:51
    
- Um, plus the arbitrary constants. Um column C1. So the, um, integration of the two, we got this one.
    
    39:00
    
- And then um, to find and iterative then again, uh, we found the function of y.
    
    39:10
    
- Yeah. The function of Y is that we, um, integration into y and z again x squared plus z one.
    
    39:24
    
- Um, so you got. All right.
    
    39:30
    
- So, um. And then we divide into question again.
    
    39:40
    
- So x squared becomes x cubed over three and then c one integral.
    
    39:44
    
- Um I mean um integration of constants. We got some c one times x.
    
    39:49
    
- And then again, that's arbitrary constancy. True, right? So, um.
    
    40:00
    
- Yeah, just remember, be careful when you integrations, you, uh, you get another arbitrary constants.
    
    40:05
    
- So, um, yeah, that's the solution, um, for this differential equations.
    
    40:11
    
- So that's what you mean by solutions to get the form of y.
    
    40:16
    
- Um, it's a function of x. So that's the, um, the methods.
    
    40:26
    
- Um, the first approach we can use, um, to finding the solutions, um, analytically.
    
    40:30
    
- All right. Right.
    
    40:38
    
- Um. So. So if you see that, um, so far we have found solutions.
    
    40:57
    
- Uh, why, um, find solutions to the differential equations, uh, which have arbitrary constant.
    
    41:03
    
- And, um, so what do we mean by c? C is to stand for any, any numbers basically.
    
    41:12
    
- Um, so if a solutions with um arbitrary constants, that's called a general solutions.
    
    41:20
    
- All right. And that means that the solutions will depend on the arbitrary constants C.
    
    41:27
    
- So what we mean by that. Maybe you illustrate that more clearly in a graph.
    
    41:34
    
- So the solution is a function. So a functions can be represented by a graph.
    
    41:47
    
- Right. So remember, the solution to a differential equation is a function.
    
    42:12
    
- And that solution functions can be sent by graph. And then we have an arbitrary constant c.
    
    42:17
    
- That means that there's a um yeah many many different possible of the graph for example.
    
    42:23
    
- So, uh, say. Yeah.
    
    42:31
    
- So for example, like this, the one in red, that's when c is equal to one.
    
    42:53
    
- Then you have um this parabola right.
    
    42:57
    
- So that's why it's a good x square. However if you change the different values.
    
    43:01
    
- So riding this blue curve, when you change the C value, then you have a different power graph, right?
    
    43:25
    
- So when c is equal to one then you have the red curve.
    
    43:30
    
- And then if you select c is equal to true then you have the blue curve.
    
    43:34
    
- And then obviously you change different values. Then you have um different yeah different parabola.
    
    43:38
    
- If you chose to be negative then you have something. Um uh, yeah.
    
    43:43
    
- On the bottom. Make sense? Yeah. Um, let me just maybe draw another one.
    
    43:48
    
- So this one, the one, um, Becker is corresponding by Cisco minus one.
    
    44:04
    
- So what I mean is that this is a family, so that we call them a family of solution,
    
    44:10
    
- or the general solutions that can be any of this curve, depending on the particular value of C.
    
    44:15
    
- Right. So yeah. So that's called a general solutions.
    
    44:21
    
- And then sometimes we can determines actually which curve we we are going to be.
    
    44:25
    
- Right. Either C go to one or 2 or 3 to the ten.
    
    44:31
    
- And that's um the numbers can be calculated uh if you are given a initial conditions.
    
    44:35
    
- All right. So we say initial conditions, then we can actually find the so-called particular solutions.
    
    44:46
    
- That means that we fix the lumber C to a particular lumber.
    
    44:53
    
- All right. And um, so and this problems this um, if it's the odd, um,
    
    44:57
    
- differential equation with initial conditions and then we call them, um, initial value problems.
    
    45:04
    
- Um, sometimes just IBP. Right?
    
    45:10
    
- Um. Yeah. So maybe let's go for this examples and then we take a break.
    
    45:15
    
- Right. So this is the initial value problems. We have a differential equations.
    
    45:43
    
- And then we have a um initial conditions. When x is equal to zero we know the y values.
    
    45:47
    
- So that's called initial conditions. And that's the differential equations.
    
    45:53
    
- And then combined together uh we can find so-called particular solutions.
    
    45:57
    
- So let's do that. Um. So the solutions, the general solutions Y can be found by doing the integrations of the right hand sides.
    
    46:01
    
- Right. So that's the um, just yeah.
    
    46:12
    
- So when you're doing the integration for the right hand side, we got something like this.
    
    46:17
    
- So we integrating the psi functions, we got say minus um cosine functions.
    
    46:27
    
- Then our free um process the arbitrary constants.
    
    46:33
    
- And then we use the initial conditions. So I see initial conditions.
    
    46:37
    
- Yeah. Okay. So substitute the numbers inside the our solutions when x is equal to zero.
    
    46:58
    
- Um the y values is equal to one. Right.
    
    47:07
    
- So when x equal to zero we got minus cosine zero over three plus this constant equal to
    
    47:11
    
- the um y values which are equal to one um given by the I c and then we just rearrange.
    
    47:17
    
- So. Yeah. So then we found the actual value was equal to four were free.
    
    47:32
    
- And then. Um, then we got these particular solutions.
    
    47:37
    
- Then we've got the particular solutions. Um. So the function y is equal to mass cosine three x over three plus this constant.
    
    48:05
    
- Now um becomes the actual values for free.
    
    48:13
    
- All right. Yeah. So that's, um. So from the general solutions with initial connections, we can also determine the, um.
    
    48:26
    
- Yeah, the arbitrary constants. All right.
    
    48:34
    
- Um, so maybe let's take a break for about five minutes, and then we'll come back to discuss, uh, more.
    
    48:37
    
- I just want to just kind of.
    
    48:50
    
- You're going? Yes. And so.
    
    49:03
    
- Both of. Um. Um.
    
    49:09
    
- Um. You know, it's all.
    
    49:15
    
- Um. Yeah. So basically what we have done is that we use this a mathematical models, um, to describe the physical process.
    
    49:21
    
- So according to the descriptions of the problems, um, we can use these equations to describe these, um, these problems.
    
    49:32
    
- Um, so the accelerations of ball is equal to these, um, gravitational constants.
    
    49:41
    
- And then with the initial conditions um at time zero the displacements go zero, and at time zero the velocity of the ball is equal to zero right.
    
    49:50
    
- So we use this term of information to describe the uh physical process.
    
    49:59
    
- So that's like the first steps in in our diagrams.
    
    50:04
    
- If you go if you go back to the diagrams, um, in the first lectures.
    
    50:07
    
- Right. So we have a physical systems and then um, suppose we understand the system well and then make some assumptions.
    
    50:20
    
- And then we can use these mathematical models, um, to describe these physical systems.
    
    50:29
    
- Right. So that's the um, the steps. And then next the um we try to solve these models to get some solutions, um,
    
    50:33
    
- from solutions we understand what's the interpretations of the systems more so that's the process we are going through, right.
    
    50:41
    
- Um, right. Right.
    
    50:50
    
- So we formulate these problems as this, um, differential equations.
    
    50:57
    
- And then the next step is try to solve that.
    
    51:03
    
- Um. The usual techniques.
    
    51:06
    
- Um, to find the right, uh, to file displacements.
    
    51:12
    
- First we found the first derivative by integrations of the right hand side.
    
    51:16
    
- Right. So, um, y dash, which is the velocity is equal to the um g times the time plus the arbitrary constant C1.
    
    51:27
    
- And then, um, the displacement functions, uh, y es, uh, during the Pi integration by finding the antiderivative again.
    
    52:06
    
- So integration of t plus c one. So integration of this function again.
    
    52:14
    
- Um, to give us the, the functions for the displacements.
    
    52:22
    
- Um, half of G2 square plus some C1 times t plus c2.
    
    52:25
    
- So c1 c2 a um uh arbitrary constants.
    
    52:30
    
- But we have the initial conditions. So we can use these conditions, um, to determine our constants.
    
    52:34
    
- Right. So we can use this um, I c to help us to determine the um.
    
    52:40
    
- You have to determine these, um, arbitrary constants.
    
    52:48
    
- So, uh, for first one, we know that, um, initial velocity is equal to zero.
    
    53:19
    
- So we substitute zero into the um time t, so it's equal to g times zero plus c one.
    
    53:25
    
- And that's equal to zero. Then we can easily see that um the constant c one is equal to zero.
    
    53:31
    
- Um, the other convictions. Um, the other connections, the uh, displacements at times zero is also zero.
    
    53:39
    
- So we've got a half times, uh, g times zero square.
    
    53:59
    
- Plus the constant c two is equal to um, the initial displacement zero.
    
    54:03
    
- And we solve that um c two is also equal to zero. So um once we found that so the particular solutions.
    
    54:08
    
- Um. Right.
    
    54:22
    
- Well. Right.
    
    55:07
    
- Um, and then so we got the particular solutions in this form.
    
    55:17
    
- And suppose that we consider when t is 10s later.
    
    55:21
    
- Um. Then it was up to you.
    
    55:25
    
- Ten inside. We got, um, g the gravitational constant.
    
    55:30
    
- Um, yeah. Sometimes you use 9.8 and sometimes they use ten.
    
    55:35
    
- Yeah. Similarly. Uh, yeah. Suppose we use the 9.8.
    
    55:39
    
- Uh, that's equal to half times 9.8 times ten square.
    
    55:42
    
- Um, that's equal to 419. That means what stem you can interpret it is physical damage that, um.
    
    55:46
    
- Right. And then, um. Then we have the, um.
    
    56:20
    
- Some physical interpretation is that that means that 10s later are the 10s the displacements of the dropping ball.
    
    56:23
    
- So if you release the ball and then in 10s time, we expect that the displacement of the ball is approximately equal to 490m.
    
    56:30
    
- Right. So. Yeah. From from these problems.
    
    56:40
    
- Um. So this simple example illustrates, um, how we can use differential equations to describe a physical problems and then, um, find solutions.
    
    56:44
    
- And then from the solutions we can actually, um, get some answers, right.
    
    56:54
    
- For example, in 10s or in five seconds or in two seconds, um, how far away is the ball?
    
    56:58
    
- Something like that. Yeah, yeah, although this is a very simple example, but still it give you some understanding, um,
    
    57:05
    
- how we can use this to help us to, um, understand the system better, understand the physical problems better.
    
    57:11
    
- Right. So that's the, um. Some simple applications about the differential equations.
    
    57:18
    
- And then in the lectures going on, we are talking about probably a bit more at once.
    
    57:25
    
- Um, studies. I want some more complicated problems, but that's the um, the logic is still going through the diagrams.
    
    57:30
    
- We, um, describe the physical systems as a differential equations and solve that, solve the equations,
    
    57:39
    
- find solutions, and then go back to interpret, uh, what the solution means physically.
    
    57:45
    
- All right. Right.
    
    57:52
    
- Um hmm. Yeah. So, I mean, the course probably a bit fast because, uh, used to be free lectures, and then we need to compressed into two lectures.
    
    57:58
    
- Um, so if that's, uh, something is, uh, not, uh, I mean, you should refer to the lecture notes for more details.
    
    58:08
    
- We may need to skip some examples, right. Due to the time.
    
    58:15
    
- So sorry about that. Um, so that for the parachute problems, um, suppose that you have, um, this extra information.
    
    58:18
    
- You are jumping from a altitude of 3000m and then, um, now, if a two people, one is 85kg and the other one is 65kg,
    
    58:28
    
- and then if they, uh, jump from the aeroplane at the same time, do you expect that?
    
    58:39
    
- Um. Have other sometimes. Um.
    
    58:43
    
- Yeah. I mean, how long you takes for this parachutist to get to the ground?
    
    58:47
    
- Right. And what's the speed? And, um, what do you think would be your wife first?
    
    58:55
    
- All right, so some of the questions that can be answered, uh, by using this modelling.
    
    59:00
    
- However, um. So the assumptions we need is not the same as the dropping ball.
    
    59:05
    
- So, because when you open up the, uh, parachute, obviously you have a very big surface area.
    
    59:12
    
- The air resistance cannot be ignored. It. Right.
    
    59:18
    
- In that case, we need to also understand, um, studies that build models with air resistance.
    
    59:22
    
- And how do we do that? Uh, we will discuss that in more details in the later lectures.
    
    59:29
    
- Right. But this is the problems is, uh, extension from the drop in ball.
    
    59:34
    
- Right. When you a jumping from an aeroplane when you open up the parachute.
    
    59:38
    
- And then obviously because the, uh, surface area, uh, you cannot assume that that's only, um, gravity.
    
    59:43
    
- You also have a very big air resistance. And how do we take that into account when we doing the models, and how do we form the models to,
    
    59:51
    
- uh, find the solutions and answer to some of the physical questions, such as things.
    
    59:59
    
- Right. So that's some of the extension we are going to discuss more, more uh, in the later lectures.
    
    1:00:04
    
- Right. But hopefully, to give you a sense,
    
    1:00:11
    
- is that how do we use this differential equations to answer some of the physical problems we are going to deal with?
    
    1:00:13
    
- Um, in real life? All right.
    
    1:00:19
    
- Yeah. Um, yeah, there's some exercise there.
    
    1:00:23
    
- And again, um, you will need to go through that, um, during the tutorial time.
    
    1:00:28
    
- Um, not in lecture times. Right.
    
    1:00:32
    
- So that's the summary of the second that shows that basically we talk about how to find solutions.
    
    1:00:36
    
- And then and also we talk about some simple things.
    
    1:00:42
    
- Um, how do we use mathematical models to describe some a simple physical phenomenons.
    
    1:00:46
    
- Right. Um. Yeah, that's the second Duchess.
    
    1:00:52
    
- Um, and then you go with the third one.
    
    1:00:56
    
- Right. Um. Um, so the next lecture is about, uh, numerical methods and, um, direction field.
    
    1:01:05
    
- So remember, um, we may be trying to solve the order differential equations we measures that FEMA offers.
    
    1:01:13
    
- Um, the first one is analytical. That means that to find the solutions, uh, analytically, usually by hand calculations.
    
    1:01:20
    
- And however, some of the equations cannot be solved directly by hand.
    
    1:01:29
    
- Then we need to use some other methods. And then that's the brief introduction.
    
    1:01:33
    
- In this lectures we talked about how to do that in uh numerical methods.
    
    1:01:37
    
- And also some um sometimes use the direction fields to help us.
    
    1:01:41
    
- Right. Um, for some equations, and actually quite a lot of them cannot be.
    
    1:01:46
    
- So, uh, cannot be solved. And analytically, that means that we cannot just directly integrate to find the solutions.
    
    1:01:53
    
- And then in that case, we need to find some other methods to find the solutions.
    
    1:02:01
    
- Um, so the first methods we are going to look at is so-called the direction field.
    
    1:02:05
    
- All right. So now from ODS, um, the functions uh, in general can be written in this form.
    
    1:02:12
    
- Um y dash or d what it is equal to functions of x and y, um x is the independent variables and y um is the dependent variables.
    
    1:02:20
    
- Uh, maybe let's look at an example to illustrate this point. So, um, for this, a, uh, differential equations, that is, form y dash y z of x plus one.
    
    1:02:30
    
- Um, we can rewrite these functions as um this form.
    
    1:02:43
    
- And. Right?
    
    1:03:12
    
- Um. So suppose that we have given a differential equation is in this form y dash plus y is x plus one.
    
    1:03:17
    
- And then we can rearrange the equation slightly to.
    
    1:03:34
    
- In this form a y dash is equal to d y with the x which is equal to this equation x plus one minus y.
    
    1:03:37
    
- So that's the, um, this is the function of this form.
    
    1:03:47
    
- And, uh, we usually call these functions. Um, we can show the direction fields, um, using this, uh, function f of x y.
    
    1:03:50
    
- Yet. We can draw the direction for you, um, using these functions f of x, y, um,
    
    1:04:21
    
- for examples, we, if you choose the value x and y two, uh, between -3 and 3.
    
    1:04:27
    
- So just to give you some. Idea.
    
    1:04:33
    
- So I choose a, um. Yeah, a lot of descriptions.
    
    1:04:38
    
- From extra, from us 3 to 3. Then wise from again.
    
    1:04:42
    
- Mask 3 to 3. And that's the value for this.
    
    1:04:47
    
- Um f x y I sorry, there's a typo. So it's no dash is just FX1.
    
    1:04:50
    
- Right. And then we put the different values into these equations.
    
    1:05:03
    
- For example, um, when x equals mass v and uh y is equal to three, we substitute u.
    
    1:05:06
    
- Um this is equal to minus five right. Something like this, right?
    
    1:05:12
    
- So you just substitute the corresponding value in x and y into this equations.
    
    1:05:25
    
- Um, so when x equal minus three and y is equal to three, so must three minus three plus one got minus five, and so on so forth.
    
    1:05:31
    
- Right. And then here you can we can draw different lines that.
    
    1:05:38
    
- Something like this. All right. So we can view these tables. Quite straightforward spot.
    
    1:05:50
    
- Just subdividing the numbers. It says.
    
    1:05:55
    
- So when y is equal to zero x equal mass, we substitute into these functions.
    
    1:06:00
    
- So we've got mass three mass zero plus one got mass two.
    
    1:06:05
    
- And then for the other values similarly we can just um view these tables um very straightforward.
    
    1:06:09
    
- Yeah. Um, in this case, the number is very straightforward. So we can fill these tables.
    
    1:06:51
    
- Um, even though if the function is a little bit more complicated, still, we can fill these tables.
    
    1:06:55
    
- Uh, yeah. It's not very difficult. We just. Yeah.
    
    1:07:00
    
- Fill the number. Um, substitute the number of x and Y and then find the corresponding number values.
    
    1:07:03
    
- So that's the, uh, this is the table for the functions.
    
    1:07:09
    
- And how do we use these tables to draw the view.
    
    1:07:13
    
- Oh. So, um, so that's the table. And then we can use these tables to help us to, uh, to draw the direction view.
    
    1:07:20
    
- So let me just draw a few examples. Right up.
    
    1:07:28
    
- So what? Okay?
    
    1:07:46
    
- Okay. All right. Let's choose this number, for example.
    
    1:07:51
    
- Um, this case is very straightforward. Um X1X equal to two and y is equal to three.
    
    1:07:54
    
- The slope is equal to zero right. So when x is equal to two.
    
    1:08:00
    
- Um so x equal to two and y's three at this point.
    
    1:08:07
    
- And then the slope is zero zero. That means that is horizontal.
    
    1:08:10
    
- So at this point there's no get to zero. So when x is equal to two.
    
    1:08:16
    
- So the x coordinate is two and a y coordinate is three.
    
    1:08:21
    
- Um in this case the slope is just say horizontal right.
    
    1:08:25
    
- And um so the other point is um similarly.
    
    1:08:30
    
- Yeah. So similarly when x is equal to one and then y's equal to two.
    
    1:08:38
    
- Um you got this zero right. So yeah zero is uh obviously is quite straightforward to draw.
    
    1:08:45
    
- And um, you can also draw the one. So when x equal to three and y is the free uh the slope is equal to one.
    
    1:08:52
    
- So that's like this form uh, one is like this.
    
    1:09:03
    
- Um. Yeah.
    
    1:09:06
    
- So it's just one. That means that, um, it's about, uh, 45 degrees, one increase by one.
    
    1:09:12
    
- Uh, y is also increased by one. So the slopes, when, uh, that's when the slope equal to one.
    
    1:09:19
    
- All right. Um, so that's the snow field. Um, when at this point, when, um, when the values.
    
    1:09:40
    
- The slope. When was a good one? Um, two.
    
    1:09:46
    
- Yeah. We can also draw two. So two is a little bit more difficult.
    
    1:09:51
    
- Is that, um. Something looks like this.
    
    1:09:57
    
- Um, so that means that the slope is equal to two. So equal to that means what?
    
    1:10:15
    
- That means that when your positions increase by one and then your y, uh, y position increase about about two.
    
    1:10:31
    
- So that's the when the slope is equal to two right.
    
    1:10:38
    
- So in this examples when the x um horizontally inclusive I one and then the vertical you need to increase by two.
    
    1:10:42
    
- And that's the slope um a two. So this is a sketch is not very accurate.
    
    1:10:49
    
- But you see that is they um it's compared to one's the slope is a bit steeper.
    
    1:10:54
    
- It says. And, uh, let me draw another one.
    
    1:11:09
    
- Uh, say, for example, I draw minus one.
    
    1:11:14
    
- Minus one is just the opposite is that when x equal to one and then the y is um, the vertical is uh decreased by one.
    
    1:11:18
    
- All right. So something looks like this. So when x increased by one um x inverse by one the y vertically y position is decreased by one.
    
    1:11:36
    
- So that's the um the minus one. Right.
    
    1:11:46
    
- So that means that when your expectations increase by one, go to the white one units and then the y vertical position is actually decrease goes down.
    
    1:11:56
    
- So that's the minus one. All right.
    
    1:12:06
    
- And then so and so forth. You can draw these. Uh, the larger number is, uh, difficult to draw by hand, but still, um, the logic is the same.
    
    1:12:15
    
- So, uh, if you use some, uh, package to allow us to draw it, um, you looks like this.
    
    1:12:24
    
- So that's the direction for you, uh, for all the different points.
    
    1:12:31
    
- All right. So this one is like the slope is zero, is the slope is one.
    
    1:12:36
    
- Uh, the snow is to go minus one. So that's the so called a slope um, direction view.
    
    1:12:43
    
- All right. So, um, you may ask, so what's the useful, uh, thing for this diversion field?
    
    1:12:52
    
- Um, this diversion field can tell us that how the solutions, um, is going with spectral time.
    
    1:12:59
    
- Right. Um, so this direction feel, um, it's, uh, it's not easy to draw by hand, but,
    
    1:13:08
    
- uh, it's more convenient, uh, if you use Matlab to draw that, um, uh, just.
    
    1:13:13
    
- Yeah. Let me just demonstrate that, um.
    
    1:13:21
    
- So first let's, uh, let's demonstrate how to use this diversion view.
    
    1:13:29
    
- So suppose we have the diversion view. And then, uh, we have some initial conditions.
    
    1:13:33
    
- Say for example, uh, initial conditions when y0 is equal to zero and uh another initial condition is y0 is equal to one.
    
    1:13:38
    
- Right. So this diversion view tells us that how the solution.
    
    1:14:11
    
- So the question for you is like May right. So you start at that initial connection.
    
    1:14:19
    
- You start with some ponds and then you follow the direction field.
    
    1:14:23
    
- For example, if you start in 500 that means that at time zero, uh, at the positions y is equal to zero or at time x we have y is zero.
    
    1:14:27
    
- And then what? The solution you go is that you go, uh, according to the direction field.
    
    1:14:39
    
- Right? Um. Yeah. So because this arrow of the direction view is pointing this way.
    
    1:14:54
    
- So when you starting at this point, you see that the solution, you just go, uh, follows the diversion view.
    
    1:15:03
    
- And that's the solution curve, right. So sometimes we cannot find the solutions directly, but we start with some initial conditions.
    
    1:15:10
    
- Then we see that um that's the solution curve or the solution functions looks like.
    
    1:15:18
    
- So that's how um. How we use the diversion feel.
    
    1:15:24
    
- Right. So this is one taste. And suppose another, uh, initial connection is y zero is equal to one.
    
    1:15:31
    
- So you start from here. Right.
    
    1:15:39
    
- So why do you always want to start from here. And then initially is horizontal.
    
    1:15:43
    
- That means that you go horizontally and then somehow you are going the direction fused in this way.
    
    1:15:48
    
- So something like this. Make sense.
    
    1:15:55
    
- So we start from here, and then you just follow what's going on with the diversion view.
    
    1:16:03
    
- Um, yeah. It tells you that the solution view looks like this.
    
    1:16:09
    
- So this diversion view tells us that, um, even though we don't have a.
    
    1:16:13
    
- Social functions in the mathematical form, but we still can draw the, uh, approximate solutions, um, of the.
    
    1:16:19
    
- Yeah. What's the solution looks like. Right. So that's the example how we can use the direction field.
    
    1:16:29
    
- Well. So this is more accurately Joanne um using Matlab.
    
    1:16:44
    
- So start from y zero is equal to zero. You follow this red curve.
    
    1:16:48
    
- If you start from here um y0 is equal to one.
    
    1:16:53
    
- And then you will follow this orange curve. Right. So basically it's just follow what this tangent field tells us.
    
    1:16:56
    
- Right. Um, yeah. So that's the code.
    
    1:17:12
    
- Um, I'll try to illustrate a little bit more.
    
    1:17:15
    
- Um, so, yeah, this this code is tell us that how do we use this, um, diversion field to draw the solutions?
    
    1:17:18
    
- Um, yeah. And.
    
    1:17:28
    
- So fun. So in these papers we also use Malachi.
    
    1:17:56
    
- Uh, yeah. Sometimes to help us to visualise the solutions a bit more.
    
    1:18:08
    
- Right. Um. Yeah.
    
    1:18:12
    
- And then. Let me.
    
    1:18:36
    
- Right. So that's, uh. So we can use the two hours to draw this diversion for you.
    
    1:18:52
    
- So what it does is that first we have a grid mesh grid, and then, uh, we have this functions, um, so a couple, it was just one.
    
    1:18:57
    
- So we have the functions which is go to x minus y plus one, uh, which is the function of x y.
    
    1:19:06
    
- And then um we use this functions a few functions to allow us to draw the decision for you.
    
    1:19:13
    
- Um, yeah. So um, that's the, some of the, the methods we are going to use.
    
    1:19:19
    
- Uh, do you have us to understand the division, feel a little bit better? Yeah.
    
    1:19:24
    
- So, um. Yeah. You can. Modify the code, um, to draw a different direction for you, right?
    
    1:19:29
    
- So in this case, the direction view we are drawing is that, um x minus y plus w, which is this one.
    
    1:19:36
    
- Um. X minus y plus one.
    
    1:19:43
    
- Right. So that's the functions we draw.
    
    1:19:49
    
- All right. Um, so that's a few methods we are going to, uh, use in some exercise.
    
    1:19:58
    
- And then the other method is called Euler methods, which is another or numerical methods to help us to,
    
    1:20:04
    
- uh, find some solutions, approximate solutions of the differential equations.
    
    1:20:10
    
- So, um, so that's the, the, the process for this or the methods that we choose the step size.
    
    1:20:17
    
- And then we start, uh, start with initial conditions and we calculate the slope, um, that direction view.
    
    1:20:24
    
- And we travel along this um distance x um, and that.
    
    1:20:31
    
- Then to find the y values corresponding me, and then we carry on and on.
    
    1:20:38
    
- Um, so maybe again that's illustrative of this example.
    
    1:20:44
    
- Not all of them would.
    
    1:20:56
    
- Things with them.
    
    1:21:03
    
- Yeah. You should say. Yeah.
    
    1:21:08
    
- All right. So let's okay, this example, um, suppose that we all are smartphones.
    
    1:21:12
    
- Firstly, we choose a step size. Um, I choose to go to one.
    
    1:21:19
    
- And then, um. So we start from x is equal to zero.
    
    1:21:26
    
- And then the next step will be equal to. 123, four and so on and so forth.
    
    1:21:30
    
- Um initially y when it was equal to one.
    
    1:21:35
    
- So that's from the initial conditions. And then the function value of x y is equal to x minus two y.
    
    1:21:39
    
- So the first valley would be x minus two.
    
    1:21:49
    
- So you comma is true. And then x y values would be uh yeah.
    
    1:21:53
    
- The original y values which is one plus.
    
    1:22:00
    
- One times the ocean view Mars two. So that gives us Mars one.
    
    1:22:06
    
- So that means that at the next time point, um, the y values go minus one, right?
    
    1:22:12
    
- So as this at time zero is to go to one and then at time one, when x equal to one the y value is equal to minus one.
    
    1:22:18
    
- So this number is uh going to going to be the next time point minus one.
    
    1:22:25
    
- And then we um again follow this formula that you go to X must try.
    
    1:22:32
    
- So that becomes one minus two times minus one.
    
    1:22:37
    
- Um, that's equal to three and then we can't go to the y value and so forth.
    
    1:22:46
    
- Right. Yeah. So this this number two.
    
    1:22:50
    
- We'll go through the next steps here. Yeah.
    
    1:22:54
    
- So you're saying this all these methods, we calculate the different x values, the corresponding y values.
    
    1:23:02
    
- Then basically what we mean is that you have five functions y of x.
    
    1:23:09
    
- So what you get from this table is that we are co-sponsoring X values, uh, for different x value.
    
    1:23:22
    
- We found the corresponding y values. So that's a lot of functions right.
    
    1:23:29
    
- We found the x value and the corresponding y values. So this is an approximate solution right.
    
    1:23:33
    
- Would. As.
    
    1:23:42
    
- So the approximate solution is that for different x we can find the corresponding y value.
    
    1:23:57
    
- So this is called a um approximate solutions.
    
    1:24:01
    
- So if you look at that, um, the always the methods is not always give us the true solution, but it give us some, some indication.
    
    1:24:08
    
- So stuff on these tampons. So that's the legs.
    
    1:24:17
    
- Why that is minus one. And that's x equal to two y is equal to this value.
    
    1:24:20
    
- And then so and so forth. Um but that's the this curve is the actual solutions the analytical solutions.
    
    1:24:24
    
- Um and then this yeah this this little triangle things is the, uh, the miracle solutions.
    
    1:24:31
    
- Um. This hotel also.
    
    1:24:49
    
- If. Mhm.
    
    1:24:56
    
- Right. So this one is the um approximate solution from the Euler method.
    
    1:25:05
    
- And then this is the analytical solutions. However this and it goes solutions sometimes do not exist or are very difficult to find.
    
    1:25:09
    
- Uh but or the Euler methods you can always follow this procedure to find these solutions.
    
    1:25:17
    
- Right. And uh yeah, obviously it's not very accurate, but there's a way to improve that.
    
    1:25:21
    
- We can, uh, change a smaller step size.
    
    1:25:27
    
- Like for example, if you change the step size to be smaller, um, the solution will be like this black curve.
    
    1:25:31
    
- So now we see that it's closer to the view solutions.
    
    1:25:37
    
- Right. So um, that means what is a smaller step size.
    
    1:25:40
    
- So the key thing we want to illustrate is that if you, uh, decrease the step size before, it's reduce the step size because one,
    
    1:26:07
    
- if you decrease to be 0.5, we see that the curve is the black curve which is closer to the viewed solutions.
    
    1:26:15
    
- Right. So the idea is that if you have smaller step size and then the numerical solution is more accurate and but you have a small step size,
    
    1:26:21
    
- then you have more, uh, calculation to do. And then it's not it's very tedious to do that by hand.
    
    1:26:30
    
- And that's why um, you need to do that in Matlab right.
    
    1:26:36
    
- So this is the curve is that you've used a different step size.
    
    1:26:40
    
- Um, if for 14 and 24, uh, one over 41 over four, one over 14 and 1.4, if the smaller you were closer to the solutions, right.
    
    1:26:44
    
- So as the step size decrease is more steps, um, you become more accurate.
    
    1:26:56
    
- So that's the idea. All right.
    
    1:27:01
    
- Um, but we will talk about how to implement honest methods in more detail.
    
    1:27:05
    
- Um, in the, um, in the following lectures.
    
    1:27:10
    
- Right. But the idea is that if you have the we don't have the view solutions, the analytic solutions,
    
    1:27:13
    
- we can use the direction fields or using the numerical methods to get us the approximate solutions.
    
    1:27:19
    
- And that can also help us understand the solutions, understand the physical systems a bit more.
    
    1:27:24
    
- Right. Um, yeah. So that's the summary of, um, his lectures.
    
    1:27:30
    
- Yeah. So we'll continue to discuss more in the tutorial time.
    
    1:27:35
    
- The.
    
    1:27:48
