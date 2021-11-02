Models Architecture planning : 



Membership : 
    -slug
    -type (free, pro, enterprise)
    -price
    -stripe plan id

UserMembership : 
    -user                       (foreignkey to default user)
    -stripe customer id
    -membership type            (foreignkey to membership)


Subscription : 
    -user membership            (foreignkey to UserMembership)
    -stripe subscription id     
    -active


Course : 
    -slug
    -title
    -description
    -allowed memberships           (foreignkey to Membership)


Lesson : 
    -slug
    -title
    -Course                         (foreignkey to Course)
    -position
    -video
    -thumbnail 

