---
context: Email — "More copy and pasted...."
audience: 
date: 2017-12-21
---

Components

As previously alluded to, Ember is made up of several components that
collectively work together in order to provide Ember OS. This document will
present each in its own section to provide better structure and facilitate
discussion and modular workflow. Before diving into each of these sections
it's helpful to first briefly describe each of these components.

   1.

   Quality & Testability. This component is meant to capture the
   requirements around building out a framework for measuring quality and
   enabling testability. One of the core philosophies being embraced in Ember
   is that each component should own its own quality. This comes in the form
   of unit tests, static code analysis, microbenchmarks, etc.
   2.

   Repo Management. This component is meant to capture the current
   limitations wherein all code must reside inside the Element repository
   (e.g. neon) and that this limits the ability of those components to be
   modular and reused by other downstream components.
   3.

   DevTools. This component includes all the various development tools such
   as distbox, dmake, dtest, xtest, etc., that will need to be updated to be
   aware of and support Ember OS.
   4.

   Ember Build. This is the build infrastructure used to bootstrap and
   build the Ember Linux OS itself. This has nothing to do with the build
   process used to build ElementOS itself.
   5.

   Libs. This includes all the 3rd party libraries that we modify in order
   to fix bugs or add functionality needed in those third party libraries
   needed by downstream consumers such as Element (e.g. sfapp, sfconfig, etc).
   This includes things such as ZooKeeper, Boost, Pion, etc.
   6.

   Base Linux OS. This is the base Linux OS itself but does not include the
   kernel, 3rd Party Libraries or Networking as those are captured in other
   components. This should be thought of as all the installed files and
   userspace tools and daemons which make up the OS proper.
   7.

   Kernel.  This is the Linux kernel itself. This component is used to
   track work we perform on the Kernel including our own custom kernel
   configuration and patches we apply to the kernel tree in the custom version
   of the kernel we deliver.
   8.

   Forge. Forge is a Platform Team developed tool responsible for
   essentially layering Element components on top of an Ember base image and
   all other required payloads into the final ElementOS deliverable. This
   replaces stagedbuild.

Networking.  This is the network configuration stack that lives on an Ember
node and is used by downstream consumers such as Element whether on an
mNode or a storage node.

--
Nicholas A. Cote
NickCo7@gmail.com
(508)735-5558
