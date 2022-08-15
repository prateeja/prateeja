# Definition(s)
1. **[Performance Problem](https://github.com/donnemartin/system-design-primer#performance-vs-scalability)** - If you have a performance problem, your system is slow for a single user.
2. **[Scalability Problem](https://github.com/donnemartin/system-design-primer#performance-vs-scalability)** - If you have a scalability problem, your system is fast for a single user but slow under heavy load.
3. **[Latency](https://github.com/donnemartin/system-design-primer#latency-vs-throughput)** - Latency is the time to perform some action or to produce some result.
4. **[Throughput](https://github.com/donnemartin/system-design-primer#latency-vs-throughput)** - Throughput is the number of such actions or results per unit of time.
5. **[Consistency](https://github.com/donnemartin/system-design-primer#cap-theorem)** - Every read receives the most recent write or an error
6. **[Availability](https://github.com/donnemartin/system-design-primer#cap-theorem)** - Every request receives a response, without guarantee that it contains the most recent version of the information
7. **[Partition Tolerance](https://github.com/donnemartin/system-design-primer#cap-theorem)** - The system continues to operate despite arbitrary partitioning due to network failures
8. **[Weak consistency](https://github.com/donnemartin/system-design-primer#consistency-patterns)** - After a write, reads may or may not see it. A best effort approach is taken. This approach is seen in systems such as memcached. Weak consistency works well in real time use cases such as VoIP, video chat, and realtime multiplayer games. For example, if you are on a phone call and lose reception for a few seconds, when you regain connection you do not hear what was spoken during connection loss.
9. **[Eventual consistency](https://github.com/donnemartin/system-design-primer#consistency-patterns)** - After a write, reads will eventually see it (typically within milliseconds). Data is replicated asynchronously. This approach is seen in systems such as DNS and email. Eventual consistency works well in highly available systems.
10. **[Strong consistency](https://github.com/donnemartin/system-design-primer#consistency-patterns)** - After a write, reads will see it. Data is replicated synchronously. This approach is seen in file systems and RDBMSes. Strong consistency works well in systems that need transactions.
11. **[Fail-over (Active-passive)](https://github.com/donnemartin/system-design-primer#availability-patterns)** - With active-passive fail-over, heartbeats are sent between the active and the passive server on standby. If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service. The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby. Only the active server handles traffic. Active-passive failover can also be referred to as master-slave failover.
12. **[Fail-over (Active-active)](https://github.com/donnemartin/system-design-primer#availability-patterns)** - In active-active, both servers are managing traffic, spreading the load between them. If the servers are public-facing, the DNS would need to know about the public IPs of both servers. If the servers are internal-facing, application logic would need to know about both servers. Active-active failover can also be referred to as master-master failover.
13. **[DNS - Domain name system](https://github.com/donnemartin/system-design-primer#domain-name-system)** - A Domain Name System (DNS) translates a domain name such as www.example.com to an IP address. DNS is hierarchical, with a few authoritative servers at the top level. Your router or ISP provides information about which DNS server(s) to contact when doing a lookup. Lower level DNS servers cache mappings, which could become stale due to DNS propagation delays. DNS results can also be cached by your browser or OS for a certain period of time, determined by the time to live (TTL). 
14. **[CDN - Content delivery network](https://github.com/donnemartin/system-design-primer#content-delivery-network)** - A content delivery network (CDN) is a globally distributed network of proxy servers, serving content from locations closer to the user. Generally, static files such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. The site's DNS resolution will tell clients which server to contact. Serving content from CDNs can significantly improve performance in two ways:
    1. Users receive content from data centers close to them
    2. Your servers do not have to serve requests that the CDN fulfills
    3. 2 types of CDN exists [Push CDNs](https://github.com/donnemartin/system-design-primer#push-cdns) & [Pull CDNs](https://github.com/donnemartin/system-design-primer#pull-cdns)
15. **[Load balancer](https://github.com/donnemartin/system-design-primer#load-balancer)** - Load balancers distribute incoming client requests to computing resources such as application servers and databases. In each case, the load balancer returns the response from the computing resource to the appropriate client. Load balancers are effective at:
    1. Preventing requests from going to unhealthy servers
    2. Preventing overloading resources
    3. Helping to eliminate a single point of failure
    
    Load balancers can be implemented with hardware (expensive) or with software such as HAProxy. 
16. **[Reverse proxy (web server)](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server)** - A reverse proxy is a web server that centralizes internal services and provides unified interfaces to the public. Requests from clients are forwarded to a server that can fulfill it before the reverse proxy returns the server's response to the client. With additional benefits like Increased security, Increased scalability and flexibility, SSL termination, Compression, Caching, Static content etc. 
17. **[]()** - 
18. **[]()** - 
19. **[]()** - 
20. **[]()** - 
21. **[]()** - 
22. **[]()** - 
23. **[]()** - 
24. **[]()** - 
