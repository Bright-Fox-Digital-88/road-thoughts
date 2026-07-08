/* quiz.js — reusable retrieval-practice widget shared across lessons.
   Markup contract:
   <div class="quiz" data-answer="1">
     <p class="q">Question text</p>
     <button class="opt">Option 0</button>
     <button class="opt">Option 1</button>
     <div class="feedback">Explanation shown after answering.</div>
   </div>
   data-answer is the 0-based index of the correct option. */
(function () {
  function wire(quiz) {
    var answer = parseInt(quiz.getAttribute('data-answer'), 10);
    var opts = Array.prototype.slice.call(quiz.querySelectorAll('.opt'));
    var feedback = quiz.querySelector('.feedback');
    var done = false;
    opts.forEach(function (opt, i) {
      opt.addEventListener('click', function () {
        if (done) return;
        done = true;
        opts.forEach(function (o, j) {
          o.disabled = true;
          if (j === answer) o.classList.add('correct');
        });
        if (i !== answer) opt.classList.add('wrong');
        if (feedback) feedback.classList.add('show');
      });
    });
  }
  document.addEventListener('DOMContentLoaded', function () {
    Array.prototype.slice.call(document.querySelectorAll('.quiz')).forEach(wire);
  });
})();
