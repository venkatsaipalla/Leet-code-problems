select distinct t1.*
from stadium t1 join stadium t2 join stadium t3
on (t1.id=t2.id-1 and t1.id=t3.id-2)
or (t1.id=t2.id+1 and t1.id=t3.id-1)
or (t1.id=t2.id+1 and t1.id=t3.id+2)

where t1.people>=100 and t2.people>=100 and t3.people>=100
order by visit_date