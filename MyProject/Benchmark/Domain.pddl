;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; 4 Op-blocks world
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain BLOCKS)
  (:requirements :strips :typing)
  (:types block)
  (:predicates (on ?x - block ?y - block)
	       (ontable ?x - block)
	       (clear ?x - block)
	       (handempty)
	       (holding ?x - block)
	       )

  (:action pick-up
	     :parameters (?x - block)
	     :precondition (and (clear ?x) (ontable ?x) (handempty))
	     :effect
	     (and (not (ontable ?x))
		   (not (clear ?x))
		   (not (handempty))
		   (holding ?x)))


  (:action put-down
	     :parameters (?x - block)
	     :precondition (holding ?x)
	     :effect
	     (and (not (holding ?x))
		   (clear ?x)
		   (handempty)
		   (ontable ?x)))

  (:action stack
	     :parameters (?x - block ?y - block)
	     :precondition (and (holding ?x) (clear ?y))
	     :effect
	     (and (not (holding ?x))
		   (not (clear ?y))
		   (clear ?x)
		   (handempty)
		   (on ?x ?y)))

  (:action unstack
	     :parameters (?x - block ?y - block)
	     :precondition (and (on ?x ?y) (clear ?x) (handempty))
	     :effect
	     (and (holding ?x)
		   (clear ?y)
		   (not (clear ?x))
		   (not (handempty))
		   (not (on ?x ?y))))

   (:method make_tower3
         :parameters (?x - block ?y - block ?z - block)
         :subgoals (and
         (task0 (make_tower_2 ?x ?y))
         (task1 (pick-up ?z))
         (task2 (stack ?z ?y))
         )
         :ordering (and
         (init < task0)
         (task0 < task1)
         (task1 < task2)
         (task2 < goal)
        ))

  (:method make_tower_2
         :parameters (?x - block ?y - block)
         :subgoals(and
            (task0 (pick-up ?x))
            (task1 (put-down ?x))
            (task2 (pick-up ?y))
            (task3 (stack ?y ?x)))
         :ordering (and
            (init < task0)
            (task0 < task1)
            (task1 < task2)
            (task2 < task3)
            (task3 < goal)
            )
  )
)