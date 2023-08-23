# Write your MySQL query statement below

# with totalReuests as
# (
# select *,count(t.client_id) as totalCount from Trips as t left join 
# users as u on t.client_id=u.users_id where
# u.banned='No'
# group by t.request_at
# )

# select t.request_at as Day,round(count(t.client_id)/tot.totalCount,2) 
# as Cancellation Rate from Trips as t join 
# totalReuests as tot on t.client_id=tot.users_id where
# # u.banned='No' and 
# (t.status='cancelled_by_driver' or t.status='cancelled_by_client' )
# group by t.request_at

# select t.request_at as Day,round(count(t.client_id)/temp.totalCount,2)
# as 'Cancellation Rate',t.status from trips as t join totalReuests as temp 
# on t.request_at=temp.request_at
# # where t.status='cancelled_by_driver' or t.status='cancelled_by_client' 
# group by t.request_at

select request_at as Day,
round(sum(case when status='cancelled_by_driver' or
status='cancelled_by_client' then 1 else 0 end )/count(status),2) 
as 'Cancellation Rate' from trips
where
client_id not in (select users_id from  users where role='client' and banned='Yes')
and
driver_id not in (select users_id from  users where role='driver' and banned='Yes')
and
request_at between "2013-10-01" and "2013-10-03"
group by request_at