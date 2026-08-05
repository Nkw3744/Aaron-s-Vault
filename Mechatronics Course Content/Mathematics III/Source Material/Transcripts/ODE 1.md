# ODE Lecture Transcript 1

> [!info] Source navigation
> [[Mathematical Modelling and Numerical ODEs|Related concept]] · [[Mathematics III Roadmap|Course roadmap]] · [[Mathematics III Overview|Subject overview]]

- I made it this far. Yeah. Let's. Um. Let's start it.
    
    0:01
    
- Um. Welcome to the course. Um, this is, uh, combi class, which is combining the math 606.
    
    0:05
    
- And also the engineering, uh, 702.
    
    0:12
    
- All right. So so engineering mathematics class, as well as the, um.
    
    0:16
    
- And modelling and differential equations. Right. So very similar topics.
    
    0:21
    
- Um. So for the engineering students we have, uh, free streams of tutorials.
    
    0:25
    
- And then for the in math class we have uh, one streams of tutorials.
    
    0:31
    
- All right. Um, so um, mostly they're the same. Um, the assessment will be slightly different.
    
    0:35
    
- I will talk about that. Um, first of all, my name is um Wenjun.
    
    0:40
    
- Um, I will be the lecture in the first half and then, um, carry, carry spoon.
    
    0:44
    
- Uh, talk to carry spoon. I will be the lecturer for the second half.
    
    0:50
    
- So, um, if you, you can find us details in the camera.
    
    0:53
    
- So that's me and that's Gabby, and that's our, uh, email address.
    
    0:56
    
- And also the, um, office, uh, office locations.
    
    1:01
    
- Um, you can find us there, um, if you you need to find us.
    
    1:05
    
- Right. Um. So most of the course materials will be on.
    
    1:09
    
- I will be on canvas. So, um, let me go through the engine course first, and then I'll also discuss the, um, math course.
    
    1:15
    
- All right. Um, and we'll do the recordings of the, uh, um, last lectures.
    
    1:24
    
- I'll upload the recordings after the lectures. Okay.
    
    1:31
    
- Um. So, uh, the cost information are basically basically the same for the engine in 02606.
    
    1:50
    
- We are doing the modelling of, uh, engineering and, uh,
    
    2:01
    
- physical phenomenons using differential equations and including the ordinary differential equations and partial differential equations.
    
    2:04
    
- And then, uh, we are discussing different techniques to solve this kind of equations during the course.
    
    2:12
    
- Um, yeah. So there's, uh, several topics. Um, this below we'll discuss that one by one.
    
    2:17
    
- Um, in the first half, we mostly focus on the, uh, techniques to solving ordinary differential equations.
    
    2:23
    
- And then in the second half, we'll discuss the techniques to solve partial differential equations.
    
    2:29
    
- And what do we mean by that? We'll discuss that in the in the coming lectures.
    
    2:34
    
- All right. And then we have a textbook, um, which is this book a.
    
    2:41
    
- Uh, engineering. Mathematics. And how do we find this textbook?
    
    2:46
    
- You can go to the course resource. If you connect to the course resource in the canvas page.
    
    2:49
    
- Okay. Yeah, so a little bit slow.
    
    2:57
    
- Um. Coffee sauce.
    
    3:06
    
- Yeah. Loading. I'll be slow.
    
    3:24
    
- What? What? That. All right.
    
    3:35
    
- Um, so if you go to the coffee sauce, then we have this book, text book, and then there's a, uh, e-book.
    
    3:48
    
- Um, yeah. You can view all night, uh, really easily.
    
    3:54
    
- And then, um, it's quite comprehensive. And then, uh, you can do some exercise.
    
    3:58
    
- Um, okay. So my one is swim.
    
    4:03
    
- Yeah, but this is a Evoque. And then you can have a look at this book and then um, we have some uh, further examples and also uh, further exercise.
    
    4:08
    
- All right. So that's um, given in the uh canvas page.
    
    4:17
    
- You can find the books there. That's the textbook. Um, so communications, uh, mostly the announcement view, uh, will make your, uh, via canvas.
    
    4:21
    
- Um, so. Yeah. Uh, so it's, uh, two hour lecture times, runs day 10 to 12, and then they, um, tutorial times depending on the 12 streams.
    
    4:32
    
- So, you know, uh, your tutorial stream time, if you're not sure, you come to see me.
    
    4:44
    
- And then, um, yeah. So that's um, that's the overview of the course.
    
    4:51
    
- And then we talk about what bit about the assessments. All right.
    
    4:56
    
- Um, the assessments of the course, uh, for the engineering students.
    
    5:06
    
- We have two assignments. Each assignment is worth 30%.
    
    5:10
    
- All right. Um. The assignment. Each assignment consists of two parts.
    
    5:14
    
- Um, it consists of a written part, which is accounts for 20% and also consists of a quiz.
    
    5:18
    
- All right. It's basically a quiz. So it's, uh, 10%, uh, for each assignment.
    
    5:24
    
- All right. So that's uh, uh, which 20% and, uh, quiz pop quiz is the 10%.
    
    5:29
    
- Uh, it's a five, uh, five quiz. Uh, five weeks.
    
    5:35
    
- So yeah, it's six 2%. So it's uh, 10% altogether.
    
    5:39
    
- So that's assignment one. Assignment two, the same thing. So, so which in fact 20%.
    
    5:43
    
- And also the weekly quiz. That's 10%. So that's total will be six 2%.
    
    5:47
    
- And also we have a 40% exams. So that's the, um, the structure.
    
    5:52
    
- And then, um, if I've seen, uh, if you go to the assignments, um.
    
    5:58
    
- Yeah. So if you see something like this, um.
    
    6:04
    
- That's right. Chris. 1234 for the first assignment.
    
    6:08
    
- Um, that's, um, the Chris will open weekly, so this is already open, um, on, uh, okay.
    
    6:12
    
- Uh, okay. Is it, um, I think Chris is already open in, um, from this Monday, and then the Chris two will be open next Monday.
    
    6:22
    
- All right. Uh, Monday, week two. Uh, Chris will be, uh, Monday week free.
    
    6:30
    
- We open nine days and then it's available on is the two day will be the 28th of August.
    
    6:34
    
- Um, the same due date, right. Or the five Chris's? Um, they have the different open day because they, um, discover for different weeks materials.
    
    6:40
    
- They have different open day, but they are all due on the 28th of August.
    
    6:48
    
- And also the which, um, part of the assignment one will be also due on day.
    
    6:53
    
- Um, yeah. Uh, okay.
    
    6:56
    
- So not here yet. Um, but, uh, okay, maybe I'll.
    
    7:00
    
- Uh, okay. I show the assignment once.
    
    7:04
    
- Okay. I should make it available. So it's again.
    
    7:10
    
- Right. So that's the. So that's the structure of assignment one.
    
    7:18
    
- We have five weekly quiz and then one written back the which is not open until the 4th of August which is B three.
    
    7:22
    
- I'm still preparing the assignment one which in but the creases are already there.
    
    7:29
    
- Um, for week one. So you can after the call, after the lecture today you may want to start.
    
    7:35
    
- You have uh, I think free, uh, free trial. Right.
    
    7:40
    
- And then you get the highest marks, uh, of all of this free trial.
    
    7:43
    
- Makes sense. So that's ten marks, and then you have free trial.
    
    7:48
    
- So, for example, the first trial, you have, uh, six mark, the second trial ten months, and then the further trial, you have also a mark.
    
    7:51
    
- And then they will be call at the time marks. Right. So, um, that's, uh, five weekly quiz.
    
    7:58
    
- And then, um, also assignment one, they are all due on the 28th of August.
    
    8:03
    
- Um, but yeah, I, I would suggest that after each week's lectures, you may try to create little bit,
    
    8:08
    
- um, to, to test your understanding of, uh, that that uh, contents.
    
    8:14
    
- Right. Um, so that's the, uh, assignment part and assignment assignment to, uh, similar structures.
    
    8:21
    
- And then exam will be the, uh, in week. I don't know, the exact date is between week 14 and 15.
    
    8:27
    
- Um, that's account for 40%. Um, that's for the engineering students.
    
    8:34
    
- Um, any questions from for the assessment?
    
    8:39
    
- But, um. So that's, um, that's for the indigenous students.
    
    8:44
    
- For the mathematics students. Slightly different. Um. Know.
    
    8:48
    
- Look. Um.
    
    8:57
    
- Yeah, for the mathematics students is a start.
    
    9:10
    
- Even if it's like, you know, in math. 606. The assignment on assignment to, uh, more or less the same, so will be same structure.
    
    9:13
    
- We have a crease and also we have a which in pop up, but the final exam is replaced by a portfolio.
    
    9:20
    
- A portfolio is most likely to be a project. All right.
    
    9:26
    
- And then you have also a written report and also your presentation.
    
    9:29
    
- So that's because the focus is slightly different for the engineering course and also for the mathematical uh, paper.
    
    9:33
    
- Right. But um, uh, essentially is that the exams, uh, of the paper is replaced by a portfolio which is,
    
    9:39
    
- consists of uh, project and also, uh, report presentation, so on, so forth.
    
    9:47
    
- All right. So, um, otherwise, um, there would be the same. If.
    
    9:51
    
- Um. Okay. Um, for the assessment.
    
    9:57
    
- Yeah. And then, um, for the course materials, um, if you go to the canvas page, uh,
    
    10:01
    
- that's the canvas page is, um, I think essentially the same for the engineering and mathematics.
    
    10:08
    
- Uh, course. So I would not. Yeah. So, yes. Uh, differentiate.
    
    10:13
    
- So basically for the, um, engineering students, for each week, we have, uh, some brief introductions and topics, and then we have expected outcomes.
    
    10:17
    
- And then before that, we actually have, uh, some to today's, uh, for you guys to maybe have a preview of what we are going to discuss,
    
    10:26
    
- because we have only two hour lecture time, and then there's actually quite a lot of to cover.
    
    10:34
    
- Right. So we expect you to, um, have a go before you come to the lectures.
    
    10:38
    
- Otherwise you may be too, too much or too, too many informations in just two hours time.
    
    10:44
    
- Right. So yeah, if, if not, uh, it's better to prepare.
    
    10:50
    
- All right. So that's, uh, some to today's, um, uh, we have, um, all these pre-recording lectures from previous years.
    
    10:54
    
- Um, so you can. Yeah, just browse through these lectures to have some idea.
    
    11:01
    
- So all this lecture from previous years and also from the last semester, uh, we have quite a lot of, uh, recordings.
    
    11:07
    
- And also you can read the textbooks and also go through some and a bit, uh, exercise as well.
    
    11:14
    
- Um, for the first week, we also have, uh, this a, um.
    
    11:20
    
- Yeah. We have also this, um. GBR Quincy.
    
    11:25
    
- All the self assessment quiz. Right. So it's not there's no mark but it's a good practice.
    
    11:33
    
- Then you maybe try a little bit to see whether you are still familiar with the engineering.
    
    11:39
    
- 602 or engineering that's two or the engineering method one materials.
    
    11:43
    
- All right. So, um, yeah, it's a good idea if you, um, you've go through this self assessment quiz as well even though it's no maths.
    
    11:48
    
- Yeah. So this is uh, some of the tougher revisions are for the engineering.
    
    11:55
    
- 601 and doing five for one. Um, to go through the quiz.
    
    12:01
    
- Yeah. And also we have um, this is my IMF, if you have seen this kind of, um.
    
    12:04
    
- It's an online exercise platform. Um, you have to use.
    
    12:11
    
- Yeah. If you haven't used it before. And then you just click that.
    
    12:14
    
- Uh, you get, uh, using the password to go through some exercise there.
    
    12:19
    
- So what we are trying to do is that we provide you enough exercise to give you up to date or refresh,
    
    12:22
    
- uh, what has been, uh, launched in the and during that, uh, one and also actually have two.
    
    12:28
    
- Right. So that's um, some of the exercises you can, um, go through.
    
    12:35
    
- And then um, and so. Yeah. During lectures, just attend the class and, um.
    
    12:41
    
- Yeah. And then after the class we have, um.
    
    12:45
    
- Uh, review the materials and also your charge. You may be charged at least.
    
    12:50
    
- Maybe give a first trial of the crystal one to see how it goes.
    
    12:54
    
- Yeah. And then, um. Yeah. All this because materials are key ones.
    
    12:59
    
- Um, that's the slice. What we are going to discuss during the course.
    
    13:05
    
- Um, uh, and also there are some other supports which is given by these slides.
    
    13:09
    
- Um, provides, uh, slides. That's um, I think it's that provided by the iate um, energy team.
    
    13:14
    
- So if you go there then there's some, some, uh, extra support you can, you can have.
    
    13:21
    
- Yeah. And also this is lecture slides. That's the previous year's recording.
    
    13:27
    
- And um, also we these are the tutorials exercise and even the answer.
    
    13:33
    
- All right. But we expect you to go through that question first and then um, and then the tutorial will go through some of the answers.
    
    13:38
    
- All right. So but this is for you to practice. Right.
    
    13:46
    
- Um, yeah. So quite a lot of materials already given in the canvas page.
    
    13:49
    
- Um, so if you can, um, please doing a little bit of, um.
    
    13:56
    
- Preparations before coming to the lectures. Um, everything makes sense.
    
    14:02
    
- Okay. Um. Any questions? All right.
    
    14:10
    
- Um, yeah. So. Okay.
    
    14:15
    
- If no questions, then we will start our actual class.
    
    14:18
    
- Um, yeah. Right.
    
    14:22
    
- So, um. Yeah. In this with this.
    
    14:55
    
- Uh, we have some introductions about this course. And also we discussed, um.
    
    14:58
    
- Uh, some techniques related to, um, our problems.
    
    15:05
    
- So this is courses, uh, about, um, the first lectures about model lines.
    
    15:08
    
- And also ode is. All right.
    
    15:13
    
- Um, so this course is, um, about how to use models, mathematical model to describe some physical or engineering phenomenons.
    
    15:14
    
- And then um, and we use it mostly so-called the differential equations.
    
    15:23
    
- And then we also discuss the techniques to solve this differential equations to get some solutions.
    
    15:28
    
- And then from the solution we get some interpretations, um, to feedback of the original questions what we try to answer.
    
    15:34
    
- Right. So that's the key idea, um, of this process, uh, we will abstract into several steps.
    
    15:41
    
- So um, models, uh, and models, we try to describe a physical phenomenon or AI or engineering problems.
    
    15:51
    
- And usually these models, uh, we resolve matter medically.
    
    15:59
    
- Um, and then the solutions can be interpreted. Right.
    
    16:05
    
- Um, as the physical understanding. What was the meaning for the solutions?
    
    16:08
    
- And then, um.
    
    16:13
    
- But the modelling side is that is not um, how to say is is not exactly science because different people can come up with different models.
    
    16:15
    
- Some are simple, some are more complicated, some are more realistic, some are, um, looking a lot of simplified assumptions.
    
    16:25
    
- Right. And then usually, uh, you don't have a correct models.
    
    16:32
    
- Right. And then but some models are more useful than others.
    
    16:36
    
- Um, yeah. So that's the key message.
    
    16:40
    
- Um, yeah.
    
    16:43
    
- So just keep keep in mind that there's no correct models, uh, per se, but usually we can use this model to help us to understand the problems.
    
    16:45
    
- So that's the, the the that's the meaning or the application of the models is not the correct model itself.
    
    16:55
    
- It's important is what the model tells us. It's important.
    
    17:02
    
- All right. And then our aim to use this model is trying to understand or translate our physical, um, principles to some musical language.
    
    17:05
    
- And then using solving this language and solving these, uh, models to help us to understand the physical problem as well.
    
    17:16
    
- So this is the engineering process. Um, yeah.
    
    17:23
    
- And can be model using differential equations. And that's the focus of our course, um, in these papers.
    
    17:27
    
- And as I mentioned, the first half, we the ordinary differential equations and the second half will be the partial differential equations.
    
    17:34
    
- Um. So let's say this is the one, um.
    
    17:41
    
- Diagrams of this modelling process, um, how we can be sum up in this, uh, four steps.
    
    17:47
    
- So suppose that we want to understand a physical system, right.
    
    17:55
    
- So we try to describe these physical systems mathematically.
    
    17:59
    
- Um that's why we come up with these models. And as I mentioned there is no correct models.
    
    18:03
    
- There are different many, many different ways to describe physical systems.
    
    18:08
    
- Um, it depends on what you try to answer. And then you can come up with maybe something more complicated or maybe something more simplistic.
    
    18:11
    
- Right. This model is used to describe these systems.
    
    18:18
    
- The model itself may not tell you enough. Well, what's the physical system?
    
    18:21
    
- Um, you want to understand? So once you have the models and then you use the techniques of mathematics to come up with some solutions, right?
    
    18:26
    
- So from the models, usually you try to find out some solutions and then use these solutions you can have for some physical interpretations.
    
    18:35
    
- What's the solution means. Um in terms of the physical systems.
    
    18:43
    
- So using the solutions how has to understand more about the original questions.
    
    18:47
    
- What we try to understand in, in um into this physics or the engineering problems.
    
    18:52
    
- Right. So that's the um, four key steps or the overview, uh, you know, diagrams.
    
    18:57
    
- How do we use the models to answer some of the physics, uh, physical problems?
    
    19:02
    
- Yeah. Um, obviously this is quite, uh, high level abstract.
    
    19:07
    
- And then you go through, uh, many, many different examples doing in the course to, um, yeah, to, to guide you, um, how this process works.
    
    19:11
    
- But this is giving you a at least an overview. Ideas.
    
    19:20
    
- Um, what we're trying to do in this course, how do we use models to help us to understand some of the problems we try to solve?
    
    19:23
    
- Right. And over the course we have many, many different examples.
    
    19:31
    
- But that's the key guiding principle, is that we always try to answer some questions and then come up with so-called models,
    
    19:34
    
- then try to solve the model to give some solutions.
    
    19:43
    
- And then the solutions usually can, uh, can be interpreted physically.
    
    19:46
    
- Then to answer our original questions. All right. And uh, some of the also the assignment questions will be also following this kind of principle.
    
    19:51
    
- So, um, let's maybe look at, uh, examples just to illustrate some of the idea.
    
    20:00
    
- Um. So the physical phenomenon phenomenon is that it's a ball is dropping from a tall buildings.
    
    20:05
    
- Right. So um, and then so we want, you know, for example, uh, what's the position of the ball as a function of time.
    
    20:12
    
- So, for example, if you drop the ball. Uh 10s later.
    
    20:20
    
- Um, what what's the, um, the position of the ball, what's the altitude of the ball after several times.
    
    20:24
    
- Right. So that's, um, this is a physical problems and, um, we want we tried to understand this question,
    
    20:31
    
- which is the position of the ball as a function of time.
    
    20:38
    
- And then, um, this this problem is a very typical question you can answer by doing a modelling.
    
    20:42
    
- All right. Yeah. Um, uh, so this is just a just list of some of questions.
    
    20:50
    
- We will return to these questions later on. Um, yeah.
    
    20:55
    
- In in in the course. I and then um, and also the first step for, for our physical problem is June.
    
    20:58
    
- Uh, so for, for solving this, um, physical problem is doing many models and, um, and this also is a diagram.
    
    21:08
    
- So an abstract way to say how do we, um.
    
    21:17
    
- Provide or develop a model. Right. So the first step is that to, um, to collect the, uh, background of the situation of the problems.
    
    21:23
    
- Right. So the when you understand the problems, uh, well, reasonably well, um, to and then to define what we try to models,
    
    21:32
    
- to define the concrete tasks we try to accomplish, uh, by doing these models.
    
    21:40
    
- So in this example is quite concrete because we want to describe the ball dropping from a buildings.
    
    21:45
    
- And then we want to see the path is that you model the position of the ball as a function of time.
    
    21:51
    
- But yeah. So this is already quite a um, concrete, uh, question we want to ask answer.
    
    21:56
    
- But in some other cases, maybe it's not as um, um, uh, concrete.
    
    22:02
    
- Maybe the question is a bit vague, right? So in that if, if the case is that the question is not quite, uh, established,
    
    22:07
    
- then you need to maybe think through brainstorming to understand what you're trying to accomplish.
    
    22:15
    
- All right. So to define the task. Yeah.
    
    22:20
    
- And then, um. Once you have an understanding of what you try to achieve,
    
    22:24
    
- then you can identify what the essential aspect of the solution you you are looking for, right?
    
    22:29
    
- So basically is to try to understand the problem well.
    
    22:36
    
- So these are the few steps to help you to understand, um, what you're trying to achieve by building a model.
    
    22:39
    
- Right. So once you have this kind of ideas then you can formulate the models by making may for example,
    
    22:46
    
- making some simplifying assumptions or to making more realistic depending on what you, uh, trying to do.
    
    22:53
    
- And then you form models and then you find the solutions.
    
    23:00
    
- Then to test the model whether the model is valid or not.
    
    23:03
    
- And then you try to find some way to improve. And after you improvement, then you see better you going fitting the background of your problems.
    
    23:07
    
- Well. So this is like a again repeating process.
    
    23:15
    
- And some of the key steps you have to go through when you try to develop a models.
    
    23:19
    
- All right. So this is always in the active process.
    
    23:24
    
- Yeah. Again this is just the high level overview. What's the key step when you try to develop a models.
    
    23:28
    
- Um. Yeah. So, um, also we can also have, uh, we can write, um, in, in, in,
    
    23:36
    
- in words while the and the diagram is that first to establish they understand the problems, uh,
    
    23:43
    
- what we are looking for and then to defining the problems, um, and then yeah,
    
    23:48
    
- basically recognise what we are trying to look, uh, look for uh, for the particular solutions.
    
    23:54
    
- We are trying to, uh, um, yeah.
    
    24:00
    
- To try to recognise or identify the solutions.
    
    24:03
    
- And then once we have, uh, understand the problem reasonably well,
    
    24:06
    
- we can try to formulate the models and then choose the find solution to test the model whether it's valid or not.
    
    24:09
    
- And then, uh, I also find some way to improve the model.
    
    24:17
    
- And the last step is that, uh, you may want to write, um, a report to say, uh, um, how you come up with this model.
    
    24:20
    
- What, uh, what's the aim and what's the steps you out to, uh, developing this model?
    
    24:27
    
- So and so forth. All right, so this is, uh, and also some, um.
    
    24:32
    
- Yeah, main steps when you're trying to model a problems.
    
    24:36
    
- Right. And then, um. Some of the tips.
    
    24:41
    
- And usually what we do in the models is so-called the Kiss principle.
    
    24:45
    
- Uh, keep it simple and stupid. That means that we always charge of, uh, generate models in.
    
    24:49
    
- The first thing is very simple, right? Um, as simple as possible.
    
    24:55
    
- So we start with, uh, very simple models.
    
    24:59
    
- And then last then we try to extend and improve the models by incorporating more functions to incorporate more detail, more features.
    
    25:02
    
- All right. You can think about like this. Yeah. So but the first step usually you come up with a models uh straightforward but it's very simple.
    
    25:11
    
- And then to extend that and improve little by little. Right.
    
    25:19
    
- Yeah. Um in practice um usually model can be simplified will be simplified.
    
    25:23
    
- Yeah. Because the to to understand the um the physical problems.
    
    25:29
    
- Right. And um, and sometimes if we use the models which we improve then we may act some complexity.
    
    25:35
    
- And then um, and also to clear any assumptions because when you're trying to simplify,
    
    25:43
    
- you want to uh, um, some usually make some assumptions to simplify the problems.
    
    25:48
    
- And that's the, um, yeah, that's the some of the, uh, tips when you're trying to doing a models.
    
    25:53
    
- All right. Um.
    
    25:59
    
- And actually in engineering and also in other, uh, in other um, area of science, the modelling is very popular or very commonly seen.
    
    26:04
    
- And um, so we just explain some of the situations, what this model can be useful.
    
    26:14
    
- Right. Um, we have we will discuss some of the models, not all of them, but at least we give you an overview,
    
    26:19
    
- uh, how these models can be applied in different area of science and engineering.
    
    26:25
    
- Right. So for example, um, if you want to estimate the, um, a person jump from aeroplanes, um,
    
    26:30
    
- we have a parachute and then, uh, we can estimate the velocity of the person, um, the person with the.
    
    26:38
    
- Yeah. Jumping from a parachute. All right. The velocity of the touches.
    
    26:45
    
- This this is another, uh, practical examples. We can use a model to house to answer these questions.
    
    26:51
    
- Right. Um, so once you open the parachute, and then we need to also consider the air resistance, so, so forth.
    
    26:56
    
- And um, so this question is discussed in details in the textbooks, which I just showed you in the canvas page.
    
    27:05
    
- Um, you can go to this, uh, sections 1.2.
    
    27:12
    
- Um, do you have a look at the backgrounds to give some more, uh, details if you are interested?
    
    27:16
    
- So what we are trying to say is that, uh, this modelling can be answer some of the questions, uh, such as these.
    
    27:21
    
- Um. And another example is that, um.
    
    27:29
    
- So. You one of the moderate displacements of a mass on a spring.
    
    27:33
    
- Right. So you have a spring and then you are a mass. Attach the spring.
    
    27:39
    
- And then we want to see how much displacement um, it is.
    
    27:42
    
- Uh, yeah. For, for spring. That can also be models.
    
    27:46
    
- Um in this questions. Yeah. And um, gives us a mass on a spring is quite a, uh, classical example in physics.
    
    27:50
    
- And then we'll come back to this, uh, examples, uh, in the later lectures.
    
    27:59
    
- All right. So this kind of fiscal problems that are modelling spring systems can be is also quite a lot of applications, other things.
    
    28:05
    
- For example, uh, what we just discussed, the spring systems can be used to uh,
    
    28:15
    
- to describe the earthquake shaking when when you have a big earthquake and they have a big buildings,
    
    28:20
    
- and then you can imagine that the big building is just like a spring moving around.
    
    28:27
    
- Right. So understand these kind of spring systems can be used to more complicated problems, right.
    
    28:30
    
- So, um, so the earthquake, you can imagine when you, um.
    
    28:37
    
- Yeah, when the buildings, uh, shaking, uh, because the earthquake is just like spring systems.
    
    28:41
    
- And then understand this kind of underlying behaviour can help us to understand more complicated stuff.
    
    28:47
    
- Right. So that's, uh, some of the ideas, um, and then, uh, other model examples, we can model the level of water in tanks,
    
    28:53
    
- um, if some inflows and outflows, and then we see that how much uh, water's in is in the tank.
    
    29:03
    
- And also the vibrating vibration systems showed us more or less like a spring.
    
    29:09
    
- Um, so yeah. Then also the, uh, electrical circuits.
    
    29:14
    
- Um, yeah, there's some of, from, from some of you from electrical engineering.
    
    29:18
    
- So, uh, uh, how to, uh, estimate the currents in the electrical circuits.
    
    29:22
    
- So that's also a very typical, uh, uh, mathematical problems, right?
    
    29:27
    
- Yeah. So. Yeah. And other than the engineering, we also have the, um.
    
    29:34
    
- Uh, biological problems can also describe by models, for example, this, uh, predator and prey models.
    
    29:38
    
- So um, yeah. And yeah, also the Covid like since the a b epidemics can be also modelled by uh, like the goal, um equations.
    
    29:45
    
- So something like this. All right. So all these um so these are the examples may not be related to the engineering directly,
    
    29:55
    
- but we just want to show you that the application of model is quite extensive.
    
    30:02
    
- Um, in in the view applications. So yeah.
    
    30:07
    
- So this course um can be useful for many, many, many different disciplines.
    
    30:10
    
- But. Right. Um, so this is, um, give you some overview and also motivations why you want to start this course.
    
    30:16
    
- And, um, then we going to some technical details.
    
    30:24
    
- Uh, and Assad mentions this in, in this papers, we usually use so-called differential equations, uh, as a model to describe a physical phenomenon.
    
    30:28
    
- And, and so what we mean by differential equations.
    
    30:38
    
- Right. So the meaning of a differential equation is actually quite straightforward.
    
    30:42
    
- It's just that equations that's involving uh derivative.
    
    30:47
    
- Right. It's not like a um um, yeah.
    
    30:51
    
- When we have uh, equations, we, I mean, when we are studying in high school, just, uh, middle school, we always see the equations.
    
    30:55
    
- Um, but what's the difference between an equation and differential equations?
    
    31:02
    
- So what we see before is something called, uh, usually called algebraic equations.
    
    31:06
    
- Right? So I mean this is a very simple equation. We can solve algebraic equations for half of x minus five equals to zero.
    
    31:46
    
- We can solve that. Um so the solution is so-called x equal to ten right.
    
    31:52
    
- So this is the algebraic equations because it doesn't involve any it just involve doesn't involve any differential.
    
    31:56
    
- Right. Uh through another example um say x squared plus two x.
    
    32:03
    
- You know, passphrase equals zero. Right.
    
    32:11
    
- So these are equations which are well familiar. This is like the quadratic equations.
    
    32:24
    
- We can factorise into different factors. And then we can see that is equal to zero.
    
    32:28
    
- If I you zero then got x equal to -1 or 2.
    
    32:33
    
- So this equations that we already quite familiar but they are called algebraic equations.
    
    32:37
    
- Um then we can solve this one using some of the standard techniques we studied in middle school.
    
    32:43
    
- High school. But what's the difference between these equations and what we are trying to, uh,
    
    32:48
    
- study in this paper is that for the differential equations we want to solve equations that's involving derivative.
    
    32:54
    
- All right. So that's the difference. Right.
    
    33:02
    
- So this is, um, all these different examples are all differential equations because they are involving, uh, derivative.
    
    34:15
    
- Right. So you can have something called say for example y dash.
    
    34:22
    
- Um, so y that's just a shorthand notation of d over d x.
    
    34:26
    
- Um, you know, can be a medieval or DCS or DUI would depend on the, the questions.
    
    34:30
    
- And then um, this is another case is that DUI t t plus t squared is equal to zero.
    
    34:35
    
- So this is equations but is involving derivative.
    
    34:40
    
- Right. Is uh some through this. And then um so this is that's uh slightly simpler.
    
    34:43
    
- This is more complicated. We have uh a second order like the um, yeah, the Y double dash or D square over the X square.
    
    34:48
    
- So that's the, um, yeah, that's the second order differentiations.
    
    34:57
    
- Um, so this but still this is, uh, this is just a differential equations because it's equations involving these differentials.
    
    35:01
    
- And this, this form is against the difference because the y have two independent variables with t and x.
    
    35:09
    
- So this is called the y with your key as that's your work x.
    
    35:17
    
- Um so this is equation involving not the just the ordinary differential equation for um partial differentials.
    
    35:22
    
- This is called a uh PDEs. All right. So this one is only with uh ordinary differentials.
    
    35:29
    
- This is called the um there's only one variables this call Odes.
    
    35:35
    
- All right. So this is also we have introduced this meeting for ODS and PDS.
    
    36:58
    
- So in this data the this this three one of three equations on the left,
    
    37:03
    
- we only have only one independent independence is usually the one on the in the bottom is in this case is D r t is the independence and also the.
    
    37:08
    
- In this case t is the independent variables in the derivative.
    
    37:17
    
- So these are called the Odes ordinary differential equations.
    
    37:21
    
- And then in these examples they um yeah we have in the bottoms uh independent variable.
    
    37:24
    
- We have two of them. Uh they are, they are key and they are Dow eggs.
    
    37:31
    
- So we have um yeah more than one independent variables.
    
    37:35
    
- So that's these, these equations called PDEs.
    
    37:38
    
- All right. So that's the meaning for all these and PDEs.
    
    37:41
    
- Yeah. Right. So the differential equations involving only one variables.
    
    37:48
    
- Independent variables. That's called ordinary differential equations Odes.
    
    37:54
    
- And that's the focus in the first half of the course. So the basically the first 6 or 7 weeks uh discuss the odds.
    
    37:58
    
- Um, yeah. And then if equations with uh, more than one independent variables, um, they're called PDEs.
    
    38:06
    
- And then we'll discuss in the second half of the course. Make sense?
    
    38:13
    
- Yeah. And this is some of the examples of the odds.
    
    38:19
    
- So, uh, what that just means is that is the why is the dependent variables and time is that is, uh, yeah.
    
    38:22
    
- The second derivative. Um. It's just.
    
    38:30
    
- Um. Okay. Yeah. Um.
    
    39:24
    
- So would you call? Um.
    
    39:29
    
- So in this example, why is the dependent variables T is independent variables.
    
    39:34
    
- So why just means that um these square y over dt square.
    
    39:39
    
- So the dependent variables over the independent variables uh differentiate twice.
    
    39:45
    
- So that's the meaning for that. Um and sometimes the independent variables can be can be ex or can be something else.
    
    39:49
    
- All right. But we usually can be quite easy to identify uh in these which are the dependent variables which are the independent variables.
    
    39:56
    
- Um and this is similarly y just free dash.
    
    40:04
    
- That just means that, uh yeah d3 y over d t cube.
    
    40:08
    
- All right. So this is just a differential free times. So this is a list of, uh, examples of all these, uh.
    
    40:14
    
- And then, um, so this illustration means that y y dash means first derivative, while the second derivative.
    
    40:23
    
- We can use d d um to represent y dash and d y squared over two square to replace y dash.
    
    40:30
    
- So this notation are also commonly used in our um in our course.
    
    40:38
    
- So yeah just make sure that you understand what they mean.
    
    40:42
    
- And then partial differential equations, just like what we, uh,
    
    40:46
    
- explain is that it is equations involve more than one, uh, uh, more than one independent variables.
    
    40:49
    
- Right. So this case is like, this is, uh, these equations for two independent variables.
    
    40:57
    
- This is a key and x and then uh, the dependent very dependent variable, you, uh, that square you watch out here square.
    
    41:03
    
- Uh, since they are square you over their X square.
    
    41:10
    
- So this equation is called a one dimensional wave equations, which we will discuss in more detail in the second half.
    
    41:14
    
- Um, so this is similarly this is the difference between these two equation is that this is just the first order differential with our key.
    
    41:20
    
- Um this is. Yeah. That's the same as this equation. Um the second order.
    
    41:28
    
- Differentiations. But now we have two independent variables.
    
    41:34
    
- So there's still a piece. And this is also called a cheat equation.
    
    41:37
    
- It's also uh quite famous um, PDEs.
    
    41:41
    
- Um so these are the, these three are the so-called the three fundamental and munchie PDEs,
    
    41:44
    
- the wave equations, the key equations, the process equations.
    
    41:50
    
- Right. Um, all these equations will be discussed in the second half of the, uh, the course, but just to.
    
    41:54
    
- Yeah, at least for you guys, uh, the moment you should recognise them.
    
    42:01
    
- They are. Oh, the, uh, PD is because they have more than one, uh, independent variables.
    
    42:05
    
- All right, so that's the meaning, um, between Odes and PDEs.
    
    42:11
    
- Right. And as, um, it's just mentioned that we use this differential equation to describe a physical phenomenon,
    
    42:18
    
- and we try to find some solutions to these equations or to these models.
    
    42:26
    
- Right. And but what do we mean by solutions. So we have a physical differential equations for example.
    
    42:30
    
- And what do we mean by solutions. A solution just means that um you satisfy these equations when you substitute into the equations.
    
    42:37
    
- Right. So let's look at uh examples. So.
    
    42:46
    
- So our solutions of the equation means that is, satisfy these equations.
    
    42:52
    
- Or make the equations valid. All right. So that's the meaning for the solutions.
    
    42:59
    
- So um let's look at examples. Um. Right.
    
    43:03
    
- So let's verify that. Uh, so the solution usually is, uh, is a pickup is a function, right?
    
    43:34
    
- It's not a number for the algebraic equations. Just what we explained in before.
    
    43:40
    
- And then the solution is usually just a number right x equal to ten or x equal to some number as well as true.
    
    43:45
    
- So for the algebraic equations the solutions usually is just number.
    
    43:51
    
- But for the differential differential equations the solutions uh are mostly uh yeah it's a functions.
    
    43:56
    
- Is a function is that the dependent variables is a functions of the independent variables.
    
    44:07
    
- So that's the solution means. All right. So a solution in in the differential equation, that means that the dependent variables uh,
    
    44:12
    
- usually y or some other case, some dependent variables is a function of the independent variables.
    
    44:56
    
- So that's what we call our solutions for the differential equations.
    
    45:02
    
- All right. Um, and then um, in these examples, we try to verify, uh, y is equal to c x square.
    
    45:10
    
- Right. So y is equal to c x squared is a function. So the dependent variables is a function of the independent variables.
    
    45:18
    
- Try to verify this. This function um this function is a solutions to the odds x y is equal to y.
    
    45:25
    
- And how do we verify it. We just check the left hand side and right hand side to see whether there's the same or not.
    
    45:32
    
- So. Right.
    
    45:39
    
- So forth. So we check the solutions. We just look at the differential equations.
    
    46:13
    
- The odds. The left hand side is equal to x times y dash.
    
    46:18
    
- Right. And then because y is you know c times x squared a differential y dash is really easy.
    
    46:23
    
- Should be equal to two times x right. So x times two times six.
    
    46:28
    
- We just um simplified it. It becomes 2CX squared.
    
    46:32
    
- So that's the left hand side. And what's our one hand side.
    
    46:37
    
- Right. So we check that is the left hand side of the equations become equal to the one hand solve equations.
    
    47:16
    
- They are both the same. So therefore these functions satisfy the ode.
    
    47:22
    
- So this is a solution. So that's the meaning for what we mean by solution right.
    
    47:27
    
- So we have for Odes. And then we find we try to find a solutions is a function.
    
    47:32
    
- It's a as a function of the independent of the dependent variables as a function of independent variables such that,
    
    47:37
    
- um, the functions should go going back to the original equations that should be satisfied.
    
    47:46
    
- All right. So the left hand side should be equal to one inside. And in this case um what is x square.
    
    47:54
    
- Let's call this solutions. Make sense?
    
    48:01
    
- Other equations that I want to try to find.
    
    48:06
    
- Functions to satisfy the equations. Yeah. And how to find that.
    
    48:09
    
- That's another problems. But but first we need to understand what we mean by solutions.
    
    48:14
    
- Right. And how do we find these functions. So that's uh that's the techniques we are going to study over the course.
    
    48:18
    
- But at least we understand how to check whether it's true or not.
    
    48:24
    
- Right. So that's the meaning, uh, for finding a solutions.
    
    48:28
    
- Um, yeah. And another example, um, you show that y is equal to C times X is also a solutions to these forms.
    
    48:36
    
- Okay. Um.
    
    48:45
    
- Um. All.
    
    49:23
    
- Um, this is an example we want to show. This function is a solution to the Odes y minus y is equal to zero.
    
    49:51
    
- And then we just check the left hand side. So why. That's right.
    
    49:58
    
- We differentiate this function c x right.
    
    50:01
    
- Because exponential differentiates always get the same thing exponential.
    
    50:05
    
- So differential tries still give you the same function c times x.
    
    50:08
    
- So c times x minus c x obviously equal to zero right.
    
    50:13
    
- So the left hand side is equal to zero. And obviously y is equal to zero.
    
    50:16
    
- And um yeah. But so yeah, hopefully this example, um, illustrates how do we check a solution?
    
    50:20
    
- You basically just, um, you have a form of solution of a function form.
    
    50:54
    
- You just substitute to the odds to see whether the left hand side ones are, uh, equal or not.
    
    50:58
    
- If they are equal. And that's a solution. If not, then that's not that.
    
    51:04
    
- That's the, um, that's the way how we check. All right.
    
    51:07
    
- Uh, yeah. This is similar. Uh, y is equal to C one star X user.
    
    51:15
    
- So we do the same thing with uh yeah.
    
    51:19
    
- The left hand side. Let me just. Right. Um, briefly this is the left hand side.
    
    51:23
    
- Sigma y double dash plus y, which is equal to.
    
    51:28
    
- All right, so this is the same idea. It's just the calculations are a bit more complicated.
    
    52:32
    
- So it's up to you. The why functions inside the left hand side.
    
    52:36
    
- So we differentiate the function tries.
    
    52:40
    
- So differential first time c one times psi function becomes an arms cosine and cosine function becomes a minus side.
    
    52:42
    
- Then we need to differentiate again um. So cosine function defined again becomes a minus minus c one times sine.
    
    52:49
    
- And then cosine x minus c two sides becomes mass c two cosine x and then plus the original wave functions we see that the cancel each other.
    
    52:56
    
- So the sum will be equal to zero which is equal to one inside.
    
    53:05
    
- And therefore um. This function is also a solutions to the problems.
    
    53:08
    
- All right. Yeah. So it's the same thing. Once you give on the phone, you just check whether the left hand side is zero, the white side.
    
    53:19
    
- But the key difficulties actually is how do we come up this fall?
    
    53:27
    
- Right. It's not a checking. Checking is I mean, it's just, uh, simple differentiations.
    
    53:30
    
- But how do we do that? How do we find this form?
    
    53:35
    
- Um, that's what we are going to study in our course, spend lots of time, and we have some exercise, and then, um.
    
    53:37
    
- Yeah, you can, you can, um, yeah, you can go through, try it yourself and then, um, please.
    
    53:44
    
- And also after the lectures, uh, it's not finished yet, and we only have the first hour and try to go through the quiz one, um, as well.
    
    53:50
    
- The quiz one again will see that this, um, will be graded will be, uh, each quiz will be 2% of your final, uh, final months.
    
    53:58
    
- Um, the reference work if you go to, uh, the books we just discussed the textbook, uh, then um, is, uh, basically this is related to chapter 1.1.
    
    54:07
    
- Okay. Yeah. So we'll take a break for about five minutes, and then we'll come back with the, um, the other part of the, the, the lectures, but it's.
    
    54:16
    
- So. I'm all right. Um, you know, uh, um, let's see if I even thought about.
    
    54:34
    
- Um. Uh, yeah. That's quite awesome.
    
    54:49
    
- Uh, and so on. Um, so, you know, our blah blah, blah, blah, blah, blah, blah, blah, blah.
    
    54:57
    
- Blah. Are you okay? Uh, you know what I'm saying to this conversation?
    
    55:13
    
- Um. Oh, yeah. It.
    
    55:21
    
- It. Her house on the way home.
    
    55:27
    
- Well. Of the comfort zone for.
    
    55:37
    
- Um. Um. Um.
    
    55:46
    
- But. Mhm.
    
    55:55
    
- Let me, um, decide. I don't know.
    
    56:03
    
- I don't. What say?
    
    56:12
    
- Uh. Well, that's.
    
    56:15
    
- Emma. My mom was inside one of my works at one stop for me.
    
    56:21
    
- So I think we all went home from.
    
    56:29
    
- Oh, um. And where the path.
    
    56:42
    
- Uh, uh, we want to see one.
    
    56:50
    
- Stop. Uh uh uh oh.
    
    56:54
    
- It's, uh. So, uh, some.
    
    56:58
    
- Mhm. Yeah. Well, uh uh uh uh, I'm not on the.
    
    57:04
    
- Uh. Right. Uh, Chinese. But. What?
    
    57:18
    
- It's not that I don't have. Time.
    
    57:24
    
- Um, but. Yeah. Um, but yeah.
    
    57:31
    
- So here's the first stuff I'll start.
    
    57:35
    
- I'm fine with posting on campus areas.
    
    57:41
    
- Probably find something to look for.
    
    57:49
    
- I just couldn't find us. Well, I mean, you have to see this one on the camera switch.
    
    57:52
    
- Have a switch? Yep. Uh, I I'm engineering all that.
    
    57:58
    
- Put it under the load balance.
    
    58:02
    
- Right. What's your name?
    
    58:06
    
- Projects of if it's available. Uh, Judy and, uh, Judy.
    
    58:11
    
- Yeah. So they should be able to see this.
    
    58:18
    
- Uh, I'm sure you know. So you to do that work. Um, wait, does it appear on canvas on the dashboard?
    
    58:26
    
- Do you have the dashboard? If not, then what will your tempo process look?
    
    58:33
    
- Yeah. Of course. Uh, because some of them you have, you have to be the favourite and show on the dashboard.
    
    58:38
    
- Um, this is the, um, uh, the quiz.
    
    58:45
    
- Um, I try to do it the other day for a little while, just,
    
    58:48
    
- just simply because I got people questions, but I'm not sure which way in here it actually is.
    
    58:51
    
- The quiz. Yes. Uh, just outside of here someplace.
    
    58:58
    
- But if you, uh, uh, uh, often you'll say that, uh, Chris just, uh, marked Chris.
    
    59:02
    
- Uh, this one is, uh, self assessment, though.
    
    59:11
    
- Okay. Yeah. Okay. So he wasn't talking.
    
    59:14
    
- He was. One.
    
    59:17
    
- Woman. Well, um, you know, um, so, um.
    
    59:22
    
- Yeah. But. All right. Um, yeah.
    
    59:30
    
- So let's, uh, let's start with study again later.
    
    59:34
    
- Hello? I'll be right up.
    
    59:38
    
- Huh? Uh, let's, uh, let's start in.
    
    59:47
    
- Five. Oh, yes.
    
    59:52
    
- Thanks for. Yeah.
    
    59:57
    
- Oh, and I'll take my on.
    
    1:00:01
    
- Oh. Yeah.
    
    1:00:10
    
- We. Not able to perform.
    
    1:00:15
    
- Well, I, um. But, um.
    
    1:00:20
    
- Yeah, let's let's start again. All right.
    
    1:00:24
    
- Um, so we just discussed, uh, what do we mean by, uh, differential equations?
    
    1:00:29
    
- And also we discuss what we mean by solutions. Um, then the next part is that how do we find these solutions?
    
    1:00:35
    
- So I generally, um, there's three different ways to do that.
    
    1:00:43
    
- Um. Because we know that the solution.
    
    1:00:48
    
- So going to solution is that functions right. So um, the solutions to Ode uh or to a PD, we expect it to be a functions.
    
    1:00:52
    
- However, it's not always, uh, possible to find a functional form.
    
    1:00:59
    
- Right. So what we discussed in this example before, we always see a loss function.
    
    1:01:04
    
- Wrong. But that's not always the case. Um.
    
    1:01:09
    
- If you cannot find the solutions. Um. Uh, I have a functional form.
    
    1:01:14
    
- There's still another way to do that. So we'll briefly mention that three ways, um, to find a function form.
    
    1:01:17
    
- Um, and then, um, yeah, in the next week, uh, coming weeks, we'll talk about specific problems.
    
    1:01:25
    
- Right. But you talk about the, the, the, the the strategy or the, the usual methods for to find the solutions.
    
    1:01:32
    
- Those are free ways. The first one is that analytically that means that we find the we try to find the least functional form of the equations.
    
    1:01:40
    
- Right. Um, yeah. Can we call that the exact formula?
    
    1:01:49
    
- So that's the, uh, analytic way. Um, the second way is called numerical.
    
    1:01:53
    
- That means that we don't know the solutions, uh, in a functional form.
    
    1:01:58
    
- So we can we can, uh, follow the solutions.
    
    1:02:02
    
- Um, we can plot the solutions as a function of time.
    
    1:02:05
    
- So that's the second numerical way. Uh, we also discussed with some example.
    
    1:02:08
    
- And then the third way is that, uh, we can actually we cannot find a solution as a function of time,
    
    1:02:13
    
- but we can describe some of the later, some of the important, uh, features of the solutions.
    
    1:02:19
    
- Right. So that's that qualitatively. All right.
    
    1:02:24
    
- So that's the three, uh, aspect of solutions we can look for.
    
    1:02:28
    
- Um, so, yeah. But we'll go through some example maybe to, um, to illustrate a little bit more.
    
    1:02:32
    
- So the first case is that we tried to find the exact formula, exact solutions.
    
    1:02:40
    
- So that another way if the if the equations in a particular form, that's usually can be done quite, um, um, quite straightforwardly.
    
    1:02:45
    
- If the differential differential equation is in this form, y dash is equal to some function of x, right?
    
    1:02:57
    
- But that's not always true for differential equations. Solutions can be more complicated.
    
    1:03:04
    
- Right. So we have a y double dash or y and so on so forth.
    
    1:03:09
    
- But for one type of differential equation which is just why does you call a f of x in
    
    1:03:13
    
- these functions we can find the exact solutions by just just to find the antiderivative.
    
    1:03:19
    
- All right. So this is one types of uh differential equations.
    
    1:03:25
    
- Right. So that's the idea for these types of differential equations y is to f of x.
    
    1:04:36
    
- We can find the exact solutions right. Uh y x we can find the functions y x by finding the antiderivative.
    
    1:04:42
    
- So let's look at some example. Right.
    
    1:04:50
    
- So in these examples we have y is equal to x squared plus cosine um two x.
    
    1:05:26
    
- So that means that um y that just means the value of the x y is equal to this form.
    
    1:05:33
    
- So um yeah. So the form to find y, basically we just find the antiderivative of these functions y.
    
    1:05:39
    
- We find the antiderivative um by integrating these functions two x square parts closer to x right.
    
    1:05:45
    
- And we find the solutions. And then um, this just uh finding the antiderivative, we found the result as um.
    
    1:05:52
    
- All right. And then the adjective will be just, um, 2 or 3 times x cubed plus side two x over two plus c.
    
    1:06:08
    
- If we have um, I mean, if you forgot, um, for this kind of techniques to finding antiderivative,
    
    1:06:16
    
- um, um, please go through some of the exercises we discussed in the, uh, canvas.
    
    1:06:22
    
- Yeah. So if you are not really familiar of this finding antiderivative, um, just go go to the chemist page.
    
    1:06:29
    
- As I mentioned that we have quite a lot of exercises.
    
    1:06:37
    
- And also the, um, the self, uh, assessment quiz that can help you to refresh, um, what is, um, how to find this kind of attitude.
    
    1:06:39
    
- All right. So this is one of the basics, uh, techniques, um, for finding the solutions of a differential equations.
    
    1:06:51
    
- Right. So you if you're not quite familiar about finding the antiderivative, um, yeah.
    
    1:06:58
    
- Please go through some of the previous, um, exercises and, um, questions to help you to refresh your memory.
    
    1:07:04
    
- All right. So this things is, uh, obviously been done in 501, uh, engineering 1 or 2.
    
    1:07:12
    
- So this is, um, you should have already done that, um, before, um.
    
    1:07:18
    
- So make sense. So this is just trying to finding the intuitive.
    
    1:07:26
    
- Um, yeah. Then this is the this is the same exercise. So we have this form.
    
    1:07:31
    
- Then we can try to find the solutions. And uh, even though in this exercise, even in the second row, you can still do the same thing.
    
    1:07:35
    
- Uh, let's let's look at this exercise. Um. All right, so we tried to find the solution.
    
    1:07:43
    
- Why? And now because the solution is so straightforward is why triple dash.
    
    1:08:00
    
- Dash is equal to x. So we just find the integrations um, one by one.
    
    1:08:06
    
- Right. So far the antiderivative of the the the right hand side uh first so two integration of two x.
    
    1:08:25
    
- So we got x square plus uh arbitrary constant c one.
    
    1:08:32
    
- So that's why dash. And then our aim is to find y and then we can do it again.
    
    1:08:36
    
- He just added duty of the right hand side again. Why now is equal to x square plus c one?
    
    1:08:51
    
- So to find y b just to find the antiderivative of the right hand side again um yeah.
    
    1:08:56
    
- The second time. And then we find the function which is equal to um.
    
    1:09:03
    
- All right. So remember why we do the integrations.
    
    1:09:13
    
- We have arbitrary constant means of integration. First we have one arbitrary constant integration.
    
    1:09:16
    
- The second time we have two arbitrary constants c1 and c2.
    
    1:09:23
    
- So and so forth. All right, so this is, um, that's if the, uh, if the differential equation is in this form in this easy com, uh,
    
    1:09:26
    
- in this particular form, then we can find the solutions by Justin, by just to find the antiderivative of the, uh, why is our functions.
    
    1:09:43
    
- All right. Right.
    
    1:09:58
    
- Um, and then if you observe that, we see that the solutions of Y is, um, yeah,
    
    1:10:04
    
- the solutions of the differential equations we usually have for arbitrary constants quite like this case,
    
    1:10:11
    
- we have, uh, this plus the apogee because then see like this case, we have uh, some functions.
    
    1:10:18
    
- You see I have uh two constants C1 and C2.
    
    1:10:23
    
- Right. So we see that, uh solutions to a differential equation,
    
    1:10:27
    
- usually we have for arbitrary constants c and then this c because this c can be any we will um verse.
    
    1:10:30
    
- That means that the solution is so-called the general solutions because is involve a different, uh, the uh arbitrary numbers.
    
    1:10:38
    
- All right. So in this case, um, in the examples in the, in the, in the last lectures,
    
    1:10:47
    
- we talked about that, uh, a solution to this equation is go to wise, you know, x square right.
    
    1:10:52
    
- So C depends thing. Um how why the um yeah.
    
    1:10:58
    
- So for different C basically is the different. Um, so maybe let me draw pictures.
    
    1:11:03
    
- Mhm. Mhm. Mhm. Mhm. Okay.
    
    1:11:32
    
- Mhm. Mhm. Right.
    
    1:11:35
    
- So what I'm trying to say is that, um. For general solutions wise, go see, x squared is actually not one functions.
    
    1:12:00
    
- It's can be many, many different functions depending on the value of c.
    
    1:12:09
    
- Right. So for example this vec curve is one uh this backup is one single one.
    
    1:12:12
    
- So this is why is x square. That's one functions but c can be other number.
    
    1:12:18
    
- Say for example c is equal to four. Then we have this green curve right.
    
    1:12:22
    
- So y is equal to four x square. This another functions.
    
    1:12:26
    
- So the solution is just one functions. And then depending on the value of c.
    
    1:12:30
    
- So we don't know which functions is actually uh can be can be the right one or can be the green one or can be the the blue one.
    
    1:12:36
    
- The blue one just means since go like the one. Makes sense.
    
    1:12:43
    
- So that's the solution itself. Um, general, that means that any curve is a solutions, right?
    
    1:12:48
    
- Um, so either the red curve or the green curve or the blue curve, they are all solutions to differential equations.
    
    1:12:55
    
- All right. Um, because any C is is okay.
    
    1:13:03
    
- Um, if there's no extra connections and C is the solution can be the red one, the green one or the, the blue one.
    
    1:13:07
    
- And in this case we call them the journal solutions. However if some some other condition is given then we can find so-called a particular solution.
    
    1:13:14
    
- Right. So that means that we can we can identify which one is the,
    
    1:13:24
    
- the the particular solutions can be that the red one or the green one or the blue one, depending on the initial conditions we are given.
    
    1:13:29
    
- All right. So that's another things. Um okay.
    
    1:13:38
    
- So maybe let me just illustrate in this examples.
    
    1:13:42
    
- Right? So in this example, what I'm trying to say is that if it's just given the odds then any see is a solutions, right.
    
    1:15:22
    
- But for this ODI we have extra connection which is that when x equals one y must equal to one.
    
    1:15:30
    
- This is y one. When x equals one, uh y is equal to one.
    
    1:15:36
    
- So maybe I write down this way. Right.
    
    1:15:40
    
- So if it's given another connection instead, when x equal to one, y value is equal to one.
    
    1:15:53
    
- Right. So this is the this is the connections y one is equal one.
    
    1:15:58
    
- Then we can determine the value of c. So how do we do that.
    
    1:16:02
    
- We just substitute u when y. When x equal to one y is equal to one.
    
    1:16:05
    
- So one is equal to c times one square x square.
    
    1:16:09
    
- So she must equal to one. So in this case y is equal to x.
    
    1:16:13
    
- Square is so called the particular solutions. So it's only this one is the solutions to both.
    
    1:16:17
    
- These are the equations with conditions. Makes sense.
    
    1:16:23
    
- Yeah. So the point is that if the equations and also we have convictions, if so-called initial conditions,
    
    1:16:29
    
- then we can determine which curve is the solution we are looking for.
    
    1:16:42
    
- Right. If it's no conditions, any curve is the solution.
    
    1:16:47
    
- But with a particular solution, conditions like this one that we can identify which curve is the solutions.
    
    1:16:50
    
- Right. That's so-called the particular solutions. So yeah that's the idea here.
    
    1:16:58
    
- So to find a particular solution we need to know some more informations which is usually called initial conditions.
    
    1:17:03
    
- Given an initial conditions then we can find the particular solutions we are looking for.
    
    1:17:09
    
- Right. So um and maybe another example.
    
    1:17:15
    
- Um, and uh, equations with an initial condition, usually called the initial value problems.
    
    1:17:25
    
- IVP. Right.
    
    1:17:31
    
- So that's the example we have on these. We have initial connections.
    
    1:18:05
    
- And then they combined together is called the initial real problems or the IVP.
    
    1:18:08
    
- Identify the solutions. Um, so. Faster solutions.
    
    1:18:15
    
- We first found the, um, the um journal solutions by finding the antiderivative.
    
    1:18:31
    
- So psi three x becomes one over three times cosine x plus arbitrary constant.
    
    1:18:37
    
- Right. But with the initial conditions we actually notice how to determine the arbitrary constants.
    
    1:18:42
    
- Right and then use the initial conditions or the ESI.
    
    1:19:10
    
- We know that we substitute you when y is equal to one, uh, x is equal to zero y.
    
    1:19:14
    
- So is y. She is one. So y is one is equal to one third times cosine three times zero plus the constant c.
    
    1:19:19
    
- And then we can solve that. Now c equal to two third right.
    
    1:19:28
    
- And this case we can find the particular solutions. So the particular solution in this case is a one third cosine three x plus two third.
    
    1:19:32
    
- Right. So that's the only one. Uh yeah one functions.
    
    1:20:02
    
- Oh sorry. Sorry. My mistake. Uh, okay okay.
    
    1:20:07
    
- Yeah. This is minus. Yeah. Integration should be minus.
    
    1:20:10
    
- Uh. Okay.
    
    1:20:21
    
- Yeah. My mistake by me doing the antiderivative should be minus one third times goes up for x plus c.
    
    1:20:26
    
- And then um, when it's up to the initial connections one is equal to minus one four times cosine three times zero plus c.
    
    1:20:33
    
- And then we can solve that c 0 to 4 free is not 2 or 3.
    
    1:20:39
    
- And now then the solutions the particular solution should be y x uh y is equal to minus one third times cosine three x plus c.
    
    1:20:44
    
- Now c is equal to four three. All right. So now we only have.
    
    1:20:53
    
- This is the um yeah. There's only one uh, wise uh functions.
    
    1:20:57
    
- Uh, it's a, it's a one particular function of x.
    
    1:21:03
    
- So that's the, the function we are looking for. This is the so-called uh, particular solution.
    
    1:21:06
    
- So if you are given the odds as well as the initial conditions, then we can find a particular solutions to the problems.
    
    1:21:11
    
- Makes sense. Okay. Uh, some exercise.
    
    1:21:28
    
- Um, I don't think we have enough time to go through that. So, um, go through that when you have, um, uh, when you are after lectures.
    
    1:21:33
    
- Right. And then so we have, um, differential equations and some solutions, and then we come back to, uh, to describe the modelling a little bit.
    
    1:21:41
    
- Um, so now we have some knowledge about the differential equations and also the solutions.
    
    1:21:47
    
- Right. So uh, we go back to the first examples we discussed in the, uh, the last lectures.
    
    1:21:52
    
- So we suppose that we drop a ball from a high price or a, uh, a building or a tower, and we want to find the positions of the ball.
    
    1:21:59
    
- All right. So how do we do that? So we see that, um.
    
    1:22:09
    
- So let's just draw some easy diagram. But so tall buildings are boys job and damn, you want to see the, uh.
    
    1:22:14
    
- The position is a function of time. So this is just a simple diagrams.
    
    1:22:33
    
- But he's got a zero. We have a ball here. And models know what.
    
    1:23:16
    
- So for example when T01 what's the position of the ball.
    
    1:23:21
    
- All right. And then from physics we know that the only force acting on the ball now is the gravity.
    
    1:23:24
    
- Right. So from physics, we know that the acceleration of the ball should be equal to, um, the gravity.
    
    1:23:30
    
- All right. So this from simple physics, we know that the acceleration of the ball is equal to the gravitational constant,
    
    1:24:21
    
- which means that y is equal to g as a nine point a metre per second.
    
    1:24:27
    
- Right. Yeah. So because there's no other force acting on the ball.
    
    1:24:32
    
- Um, and also the that makes some assumption, which is that we assume that the air resistance is the critical.
    
    1:24:37
    
- Right. You can can be ignored because the boy's heavy.
    
    1:24:44
    
- Right. So that's what we mean by modelling is that um.
    
    1:24:52
    
- So we have described the systems and then we have some make some assumptions.
    
    1:24:56
    
- Uh, we assume that the system is um, yeah, is negligible.
    
    1:25:00
    
- But in some other cases if the ball is quite small, uh, if the surface is quite big,
    
    1:25:06
    
- like when you parachute, then the air resistance cannot be ignored.
    
    1:25:12
    
- It. Right. So it depends on the questions. But in this case because the is heavy and then, um, you only consider there's no air resistance.
    
    1:25:16
    
- The only, uh, force is the gravity. So we now have this.
    
    1:25:24
    
- So this is so-called the model or the equations. Right.
    
    1:25:28
    
- So from this, uh, assumptions and from the physical, uh, problems for physical descriptions, we, we come up with so-called models, model equations.
    
    1:25:31
    
- Um, is in this form, right? So obviously this is a quite straightforward, uh, examples.
    
    1:25:42
    
- Um, hopefully, but still give you the idea, um, what we mean by, uh, modelling and, uh, using differential equations.
    
    1:25:48
    
- And then in this case we actually can find out our solutions by just doing the equations.
    
    1:25:56
    
- Right. So g is a constant. And then we just in the equations that constant um tries to find out the um yeah the solutions.
    
    1:26:01
    
- Right. And then, um, we can describe these problems using these mathematic equations, which is that each of these y is equal to g.
    
    1:26:55
    
- And then we also have two initial conditions. Um the first field conditions.
    
    1:27:03
    
- The first connection is that y zero is zero. So you drop the ball at uh position zero, for example.
    
    1:27:11
    
- And then the second connection. Is that why that's zero. Why is that.
    
    1:27:17
    
- Um the first derivative is the velocity. Right. So because you release that um at time zero.
    
    1:27:21
    
- So at that point there's no speed. So y zero is equal to zero.
    
    1:27:28
    
- Make sense? So that's the two, uh, connections we can use, um, to find our solutions.
    
    1:27:33
    
- So. Yeah. Then we can solve the problems.
    
    1:27:39
    
- Um. All right.
    
    1:27:43
    
- And then we can solve these problems using our, um, technique we just discussed in iterative.
    
    1:29:08
    
- Right. So the first one, uh, from what we can find, pi integration, uh, why has I.
    
    1:29:14
    
- So I have, uh, arbitrary constants C1. And then we use the first connections because y zero is equal to zero right.
    
    1:29:20
    
- So we substitute zero inside. Um that gives us c one must be equal to zero.
    
    1:29:28
    
- Um yeah. So zero plus C100100.
    
    1:29:32
    
- So we know that y t uh is equal to g.
    
    1:29:36
    
- And then you find the key is the positions y.
    
    1:29:39
    
- We need to integrate the y and z again for the antiderivative again.
    
    1:29:43
    
- So we find that in the equation of gt becomes half gt square plus c2.
    
    1:29:48
    
- And then we use the other initial conditions. Uh job from position 0Y0 is equal to zero.
    
    1:29:53
    
- We solve that c2 also equal to zero. So now the solution becomes y t is equal to half g t square.
    
    1:29:59
    
- So that means what that means that at any time point we know in theory what's the position of the ball half g t squared.
    
    1:30:05
    
- Right. So going back uh.
    
    1:30:14
    
- But so going back to. So once we found this, uh, solutions, uh, what is a function of time?
    
    1:30:35
    
- Then we can go back to the questions. Right. So at time zero the position is zero.
    
    1:30:43
    
- And then the only force is gravity.
    
    1:30:47
    
- And then we know that for example t0 one we substitute y one is equal to half g t squared half g which is about 4.9m.
    
    1:30:49
    
- So it's a 4.9m away from the initial positions.
    
    1:30:58
    
- Right. So so once you get the solutions we can get some physical interpretations.
    
    1:31:03
    
- What's the mean. What's the meaning for that? Is that after some time then we know that how far away is dropping?
    
    1:31:08
    
- The ball is dropping from the initial point. Makes sense.
    
    1:31:14
    
- So, yeah. So this is the, um, a simple example, but at least give you some ideas is that we use this modelling to describe the physical problems.
    
    1:31:20
    
- And then we once we got the solutions um, in this form,
    
    1:31:29
    
- then we know that in these solutions that tells us something about the original physical systems, for example, we can touch that.
    
    1:31:33
    
- He tells us that after one seconds, um, physical one one seconds, um, the ball is dropping 4.9m away from the initial positions.
    
    1:31:40
    
- All right. So this is the starting point zero seconds.
    
    1:31:53
    
- And after one seconds the ball is about 4.9m away.
    
    1:31:56
    
- Makes sense. Okay, so this is a, uh, simple examples to illustrate.
    
    1:32:03
    
- How do we use differential equations to help us to understand our physical problems?
    
    1:32:10
    
- Um, then the problems can be extended, as I mentioned.
    
    1:32:15
    
- Um, we can, uh, models the, uh, the speed of parallel purchases.
    
    1:32:19
    
- That means that a person that have personal time and then, um, but when you open the parachute and in the beginning,
    
    1:32:25
    
- um, maybe if there's a free fall, then the the positions just, uh, have to square, right?
    
    1:32:33
    
- The same as the ball. But when you open the parachute, obviously the air resistance cannot be ignored.
    
    1:32:39
    
- It that you need to consider another odes to solve these problems.
    
    1:32:44
    
- Right. Um, so there are some quite interesting dynamics.
    
    1:32:48
    
- Um, you can look for. Yeah. So you to make sure that the speed when you're landing is not too far and then so and so forth.
    
    1:32:52
    
- So yeah. So that's how you decide how much time you want to release the parachutes.
    
    1:32:59
    
- Right. Something like this. So everything can be calculated.
    
    1:33:05
    
- Um, in this kind of models. Um, so the problem is, um, can be quite interesting.
    
    1:33:08
    
- Um, but we will not discuss in detail in this course, uh, maybe a little bit more, but, um, there's, uh, as I mentioned in the textbook,
    
    1:33:14
    
- they have, uh, quite data examples about this, uh, this case, um, if you're interested, please go to this, uh.
    
    1:33:22
    
- The textbooks give you more exam, uh, more informations.
    
    1:33:32
    
- Uh. [INAUDIBLE]. Yeah, yeah.
    
    1:33:36
    
- In section 1.2. Question 15. Basically, using our ideas, we can already solve these kind of more complicated problems.
    
    1:33:40
    
- Right. How to model a person jumping from, uh, a plane using a parachute?
    
    1:33:48
    
- Yep. How much time to release the process and so forth.
    
    1:33:56
    
- So this is quite, uh, interesting problems. You can, um.
    
    1:34:00
    
- Yeah, you can have a go, um, at this, uh, in this chapter.
    
    1:34:04
    
- Right. So that's the first part.
    
    1:34:10
    
- Um, basically we discussed how to use the integral solutions, analytical methods to find solutions to a differential equations.
    
    1:34:12
    
- Right. So that's the um, that's the first method we discuss and then an index.
    
    1:34:20
    
- And then uh, we also measures the numerical and then quantitatively uh, briefly uh, as well.
    
    1:34:25
    
- So that's the first method is the analytical methods.
    
    1:34:33
    
- And then but sometimes it's not possible to find a solution.
    
    1:34:37
    
- And then this code and then we can use other methods.
    
    1:34:42
    
- Um, so so-called the numerical methods or the um quantitative methods to understand the solutions.
    
    1:34:45
    
- So that's the two things you briefly introduce, which is the numerical methods and also the so-called the direction field.
    
    1:34:52
    
- All right. So these two methods was sort of an analytical solution.
    
    1:34:59
    
- Just design a persona so you have a form for that. That's analytical.
    
    1:35:06
    
- So what we discussed here you don't have a form of the functions right.
    
    1:35:09
    
- Um so this two methods will not give you the exact form of the functions, but you give you some idea or some, some understanding of the solutions.
    
    1:35:14
    
- All right. So we'll discuss um, briefly. Right.
    
    1:35:22
    
- So add in actual facts. Differential equation is quite hard to solve.
    
    1:35:27
    
- So it's not like just the simple case we discussed. Usually you don't.
    
    1:35:31
    
- I mean, if it's a question the model is complicated. You cannot find solutions like what we did.
    
    1:35:36
    
- All right. Then what we can do is that we understand some of the features of the solutions.
    
    1:35:42
    
- So one of the methods we used is called the diagram view.
    
    1:35:47
    
- So for general um differential equations is becomes not just a function of x is a function of x and y.
    
    1:35:51
    
- In this case you cannot just directly find the antiderivative.
    
    1:35:58
    
- Okay. And then in most uh it's quite likely you, you don't accept some, uh, functional form.
    
    1:36:02
    
- Then what you can do. All right. So let's look at this example.
    
    1:36:09
    
- Um, in this case we have functions y dash plus y is equal to x plus one.
    
    1:36:14
    
- Um. So for differential equations y dash plus ones you do x plus one.
    
    1:36:20
    
- And then we have a little bit. So why do you just go x plus y minus y?
    
    1:36:46
    
- And because now we have a y on the y has. You cannot just directly find the administrative of the function y.
    
    1:36:55
    
- Right. So we cannot just integrations. Right. Because you have an unknown y on the right hand side.
    
    1:37:01
    
- So the methods we just discussed doesn't work anymore right.
    
    1:37:06
    
- You cannot find the initiative this other way to solve this problems.
    
    1:37:10
    
- But, uh, we will not discuss in details that in this week.
    
    1:37:14
    
- We will discuss that a bit later. Um, in the I think in the next week we'll talk about how to solve this problem using analytical methods.
    
    1:37:17
    
- But if the problems have become a bit more complicated than you can't even solve using an equal method.
    
    1:37:24
    
- But how do we do the numerical method direction view?
    
    1:37:30
    
- So this is now y. Dash is a function of x and y right.
    
    1:37:34
    
- So in general you can think about this is a functions. Um, a function of x and y.
    
    1:37:38
    
- So this this. So the y hand side is a function of x and y.
    
    1:37:45
    
- That means that for different x and y values y dash will be different.
    
    1:37:48
    
- Okay. Then we can come up with so called a table. So suppose that we want to show the uh the proc for between x and y between -3 and 3 okay.
    
    1:37:53
    
- So what do we do. So that's the uh the function y dash is equal to x minus y plus one.
    
    1:38:04
    
- And then we just come up with tables such that say for example, just taking the, uh, integers from us 3 to 3.
    
    1:38:10
    
- Uh, y is also from us 3 to 3, right. So just fill in the table.
    
    1:38:18
    
- But it's straightforward. So lattice lumber just must free must free pass one.
    
    1:38:22
    
- That's why must five. Yeah.
    
    1:38:28
    
- So, um, so just getting the numbers, right.
    
    1:38:42
    
- So when you do mass and once you freeze or you substitute you into this, Y and Z, we've got mass fine mass for mass famous two, one, two and one.
    
    1:38:45
    
- So as of all I can fill in a second now is the same thing was for.
    
    1:38:54
    
- Right. So what I'm trying to say is that we can view this table very, very straightforward.
    
    1:39:05
    
- And each this number we present as low. Um, so this number is is mean has some meaning because this number represent the slope y f dash.
    
    1:39:12
    
- Right. That means um yeah. This number represents what the x.
    
    1:39:22
    
- Right. So what I'm trying to say is that these tables is represent some physical information about you are awake.
    
    1:39:41
    
- You are what that means that how the Y is changing of X, right, is according to this number.
    
    1:39:48
    
- So we can draw I mean this table is very easy to fill in.
    
    1:39:54
    
- Um, just some easy calculations.
    
    1:39:58
    
- And then so the direction field, that means that each of this point, this grid pawn has some um, is according to this number.
    
    1:40:01
    
- Right? This the slope is according to this number. Uh, for example, when y is equal to zero, that means that when exchange y doesn't change.
    
    1:40:09
    
- Right? So, um. So.
    
    1:40:16
    
- So for example, when x equal to minus three and y is two.
    
    1:40:19
    
- That's like this point. Right.
    
    1:40:24
    
- So at this point we know that, um, is the is a horizontal because when exchange y doesn't change the style of the X, right.
    
    1:40:33
    
- And then for example, at one when I, when the slope is equal to one, that means that.
    
    1:40:42
    
- Um, that's like the 45 degrees. So when it's increased by one is also increased by one.
    
    1:40:53
    
- That's the slope. Um, at these different points.
    
    1:40:58
    
- Like any other business. Yeah. So we can complete this for you using this number.
    
    1:41:03
    
- All right. So compared together, um, we just using the Matlab to show that a bit easier.
    
    1:41:09
    
- So you see that in, in this light that's just like, uh horizontal.
    
    1:41:15
    
- That doesn't change. And then one does like this. And then at a the other point is become more steep because the slope is getting bigger and bigger.
    
    1:41:19
    
- So in this point it's steeper. And this point is going towards this one is going forward, uh, upwards.
    
    1:41:28
    
- But based on this number, this is so called the direction view.
    
    1:41:34
    
- We can draw a diagram like this. Right. Show a diagram of direction view.
    
    1:41:38
    
- And then from this direction field we know that what the solution looks like.
    
    1:41:43
    
- So what do you mean by that. Is that um for any points you start at a point.
    
    1:41:47
    
- Then the the solution will go according to the direction view.
    
    1:41:52
    
- Right. So this is just like a map. So you start at this point you were going through this, uh, torsion field and then give us a, a graph solutions.
    
    1:41:58
    
- Graphical solutions. Right.
    
    1:42:09
    
- So with with the tables we got the distortion field.
    
    1:42:12
    
- We are with this direction field we can show our solutions. So for example suppose I draw at this point I start at this point.
    
    1:42:16
    
- Right. So from this direction field you start at this point you mostly follow these directions.
    
    1:42:35
    
- Then you see you got a solution to this. So what was this.
    
    1:42:40
    
- This is a solution. Well this is a function we went out.
    
    1:42:44
    
- We don't know the exact functional form, but this is a function because for the x value for the independent values we have a y values.
    
    1:42:47
    
- So this red curve, even though it's not half x square or uh how or x cubed or something, but still it's a function is a solutions.
    
    1:42:55
    
- Does that make sense. Yeah. So we try to remember for this differential equations.
    
    1:43:06
    
- We tried to get something like this y. X is equal to something.
    
    1:43:24
    
- That's the function we are looking for. Okay.
    
    1:43:28
    
- And then, um, even though we don't have an exact form of the solutions, but we know for different x value,
    
    1:43:30
    
- we know the y values that in some cases already considered a solutions.
    
    1:43:38
    
- Right. So that that's the idea. Um, we don't know the exact form of the solution, but we know that what's the graphical looks like?
    
    1:43:43
    
- Say for example, when x equal to one, we know that x is approximately equal to zero or x equal to some number.
    
    1:43:49
    
- So that's the solution we are looking for. So using this direction view we can still have approximate solutions.
    
    1:43:55
    
- Graphical solution. So this is one page of solutions.
    
    1:44:01
    
- All right. So that's the one methods numerical uh thousand view.
    
    1:44:05
    
- And then the um so this is the Matlab code.
    
    1:44:10
    
- Um you can try that in the tutorial time you produce this kind of um, uh, direction view that helps us to understand the problems more easily.
    
    1:44:13
    
- All right. So that's the um, the, the Matlab code to generate this talk.
    
    1:44:22
    
- And then the other method is that we can use the so-called Euler's methods, um, to, to calculate the value of the solutions.
    
    1:44:27
    
- Right. Um. Yeah, that's some steps to go through.
    
    1:44:35
    
- Uh, we were just mentioned briefly. We will talk about that in more detail in the in next week's lectures because we don't have enough time.
    
    1:44:40
    
- But let's go through one very, uh, simple example to illustrate this method.
    
    1:44:47
    
- So you have uh, uh, odds and then you have, uh, initial conditions.
    
    1:44:52
    
- Right. Then what we do is that, um. We step by step size when equal to one.
    
    1:44:57
    
- Then we find the slope at different points.
    
    1:45:04
    
- Okay. Um, yeah. Let me just maybe just illustrate very quickly.
    
    1:45:09
    
- It. Right.
    
    1:45:19
    
- So in the first row when x equals zero y's,
    
    1:45:49
    
- given that one does the initial connections and then the function the slope is equal to x minus two y which means you two.
    
    1:45:52
    
- That's equal to minus two right. So that's the slope. And then we want to find the x y values right.
    
    1:46:00
    
- So how do we find it looks? Well, it was just the, uh, the the the previous step y value plus the step size times the slope.
    
    1:46:42
    
- The step size. We choose to be one. All right. So one times the snow slope is equal to minus two.
    
    1:46:51
    
- So then we know that that x equal to one y is approximately equal to minus one.
    
    1:46:57
    
- So that's the solution we are looking for. So that we can carry on this step.
    
    1:47:02
    
- So now x equal to one y is equal to minus one.
    
    1:47:06
    
- And then the slope. Yeah.
    
    1:47:10
    
- So similarly for the next time. So when x equal to one with.
    
    1:47:38
    
- Now. Yeah. Because y one in the y one is one minus one.
    
    1:47:43
    
- We substitute here. And the slope is x minus two y. So it's one minus two times.
    
    1:47:47
    
- Now why is u minus one. So this is not going to go free right.
    
    1:47:51
    
- And then so that means that at the next time points y two is equal to y one plus the step size h times the slope.
    
    1:47:55
    
- So it's one times three so simplifies to two.
    
    1:48:04
    
- That means that at x equal to two y is equal to two using this method.
    
    1:48:07
    
- And then we can, uh, for this this kind of, uh, algorithms or these steps.
    
    1:48:13
    
- We found the different X values. We have the Y values.
    
    1:48:18
    
- Right? So we know that if you, you, uh, you plug this pawns in a graph, that means that, um.
    
    1:48:21
    
- Right. And what I'm trying to say is that using these kind of these steps, we can find a different value for y.
    
    1:49:06
    
- So at x equals 0YZ1X0110 minus one 02102.
    
    1:49:13
    
- So that's what we calculate. And then we carry on. We found that when x equal to three we got zero and zero.
    
    1:49:20
    
- For we got y is equal to three right. So obviously this is not a very smooth functions.
    
    1:49:26
    
- But still we can know that for different x value we can get the y values right.
    
    1:49:31
    
- So this is kind of a solutions. It's uh it's not an exact solutions but this is called numerical solutions.
    
    1:49:36
    
- So then it goes for different x value.
    
    1:49:55
    
- We know the y value. So that's the numerical solution for the functions right.
    
    1:49:59
    
- And then if your function is actually the step size we choose x quite.
    
    1:50:03
    
- That is the one. If you change to say for for example 0.1 you have a very smooth solutions right.
    
    1:50:09
    
- But now obviously the step is much more. So you need to do a lot of calculations.
    
    1:50:16
    
- But you see that, that, that uh, the idea is that if you have a small step size, you can get a quite nice function for y x, right?
    
    1:50:21
    
- So again, even though you don't have the functional form of y, you have a very good graphical representation of y.
    
    1:50:30
    
- So this is called a numerical solutions or the direction field.
    
    1:50:38
    
- So this two methods doesn't give you the exact form of y but still give you some idea of what the solution looks like graphically.
    
    1:50:42
    
- So it makes sense. Yeah. But, um. In fact, if you can get a, um, functional form, that will be more information.
    
    1:50:51
    
- Um, in this case, actually, we'll discuss in the next few weeks how do we get the functional form right.
    
    1:50:59
    
- But this graphical form test, you give you some insight.
    
    1:51:05
    
- The functional form is useful. The classical form can help you to understand the problems.
    
    1:51:09
    
- All right. Um, yeah.
    
    1:51:14
    
- So that basically the, uh, key idea of this week, um, again, please review the lecture materials and then go through some of the quiz questions.
    
    1:51:16
    
- Um, and also in next week we'll go through some of the code. We don't have time today, but we'll go through that, uh, in next week's lectures.
    
    1:51:26
    
- Right. Um, so the textbook materials 1.24 are for these lectures.
    
    1:51:34
