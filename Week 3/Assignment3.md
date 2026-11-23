What is Amortized Analysis and What Does It Do?
What it means (in simple terms)
Amortized Analysis is a way of finding the average time an operation takes over many tries, instead of judging it by one single slow moment.
Simple Everyday Example
Imagine buying a ₦2,000 notebook at the start of the semester, and then writing notes in it for 20 lectures:
* On Day 1, you spent ₦2,000 (expensive!).
* On Days 2 to 20, you spent ₦0 because you already had the notebook.
* If you spread that ₦2,000 across all 20 lectures (₦2,000/20), it really only cost you ₦100 per lecture.

What does it do in Data Structures?
It helps us see if a data structure is actually fast in real life.
For example, in a Dynamic Array:
* Most times when you .append() an item, there is already extra space waiting, so it happens instantly.
* Every once in a while, the array gets completely full. When that happens, Python has to create a bigger array behind the scenes and copy all the old items over—which takes a bit of extra time.
* Amortized analysis averages out that one slow copying step across all the fast .append() steps, showing us that adding items to a dynamic array is still super fast on average.
