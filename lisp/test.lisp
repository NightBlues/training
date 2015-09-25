;; (progn
  ;; (defparameter mylist (make-array 3 :fill-pointer 0 :adjustable t))
;;   (print mylist)
;;   (vector-push 2 mylist)
;;   (vector-push 3 mylist)
;;   (vector-push 4 mylist)
;;   (vector-push 5 mylist)
;;   (vector-push-extend 6 mylist)
;;   (print (elt mylist 0))
;;   (setf (elt mylist 1) 12)
;;   (print mylist))


;; (defun swap (a b)
;;   "Swap two fields"
;;   (let ((tmp a))
;;     (setf a b)
;;     (setf b tmp)))

(defmacro swap (array a b)
  "Swap two fields"
  `(let ((tmp (elt ,array ,a)))
    (setf (elt ,array ,a) (elt ,array ,b))
    (setf (elt ,array ,b) tmp)))

(defun insert-sort (mylist)
  (dotimes (i (length mylist) mylist)
    (do ((j i (1- j))) ((or (< j 1) (> (elt mylist j) (elt mylist (1- j)))))
      (swap mylist j (1- j)))))

(defun main (argv)
  (let* ((mylist (map 'vector 'parse-integer (cdr argv))))
    (princ (format nil "~{~A~^ ~}~&" (map 'list 'identity (insert-sort mylist))))))

(main *posix-argv*)

;; (main (list "sbcl" "5" "2" "8" "3" "6" "10" "4"))

