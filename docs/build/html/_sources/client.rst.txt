Client
======

Represents a client for all endpoints.

   .. rubric:: *property* version
      :name: property-version

   | Version of the client.
   | `string <https://docs.python.org/3/library/stdtypes.html#str>`__

..

   .. rubric:: *property* canvas
      :name: property-canvas

   | Client for fetching canvas related endpoints.
   | `CanvasClient <#CanvasClient>`__

   .. rubric:: *property* misc
      :name: property-misc

   | Client for fetching anime and misc endpoints.
   | `MiscClient <#MiscClient>`__

..

   .. rubric:: *property* animal
      :name: property-animal

   | Client for fetching animal related endpoints.
   | `AnimalClient <#AnimalClient>`__

   .. rubric:: *method* close()
      :name: method-close

   Close the client
