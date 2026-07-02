---
context: Email — "Solidfire product overview"
audience: 
date: 2017-12-21
---

The solidfire product is very flexible. It boasts the ability to be
non-disruptive, granular, allowing mixed hardware (SF Nodes - a node is our
storage hardware), Scale out, scale back, and no forklift upgrades.

SF does not use RAID to protect data, everything is written to two nodes in
the system. When a drive or node fails the system auto heals to restore
redundancy automatically. Each node has CPU, storage, memory, and
networking. More nodes provide more throughput and computational resources
resulting in faster rebuild times.

We use cache cards to cache data to be written to disk. We also have
dedicated drives, slice drives, where metadata is written to.

That is standard Solidfire product also known as AFA.

Ember is the new kernel we are developing on, it allows us to develop our
own kernel instead of building on a vanilla ubuntu instance. More
customization and understanding on how the kernel is operating, gives us
more control.

HCI is the hot new product, but that is outside of element. We are calling
that SFPrime so no need to look at that.

This meeting is almost over. I'm going to try and track down someone on the
element team to pick their brain a bit more on day to day.

--
Nicholas A. Cote
NickCo7@gmail.com
(508)735-5558
