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
11. **[]()** - 
12. **[]()** - 
13. **[]()** - 
14. **[]()** - 
15. **[]()** - 
16. **[]()** - 
