;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; 4 Op-blocks world
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain BLOCKS)
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

  (:action destroy_tower
          :parameters (?x - block ?y - block)
          :precondition (and (ontable ?x) (on ?x ?y) (clear ?y) (handempty))
          :effect
          (and (ontable ?y)
           (not (on ?x ?y))
           (clear ?x)))
)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  (:action make_2_lvl_tower
          :parameters (?x - block ?y - block)
          :precondition (and (ontable ?x) (ontable ?y) (clear ?x) (clear y?))
          :effect
          (and (not (ontable ?y))
           (not (clear x?))
           (on ?x ?y)))

  (:action make_4_lvl_tower
          :parameters (?x - block ?y - block ?z - block ?w - block)
          :precondition (and (ontable ?x) (ontable ?y) (ontable ?z) (ontable ?w)
          (clear ?x) (clear ?y) (clear ?z) (clear ?w))
          :effect
          (and (not (ontable ?y)) (not (ontable ?z)) (not (ontable ?w))
           (not (clear x?)) (not (clear y?)) (not (clear z?))
           (on ?x ?y) (on ?y ?z) (on ?z ?w)))
