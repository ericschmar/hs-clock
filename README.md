# hs-clock

## Timeline
- [x] August 2017 - Identify a faculty advisor and a feasible project with an appropriate scope.  
- [x] September 2017 - Complete the first presentation (roughly project requirements).  
- [x] October 2017 - Complete second presentation (roughly revised requirements and design).  
- [ ] November 2017 - Project implementation and testing, schedule final public presentation.  
- [ ] December 2017 - Complete final presentation and upload all documents (design artifacts) and
code to course file drop box for the Project Artifacts assignment.

September
- [x] Pull a current subset of active decks
- [ ] Begin labeling labeling
- [x] Begin initial design on NN   
- [x] Layers, convolution (?), output function  
30 nodes per layer, 3 layers, activation=reLU, output=softmax  
https://keras.io/getting-started/sequential-model-guide/
- [x] Set up Keras, Tensor Flow, and Flask  

October  
- [x] Begin front end work  
- [x] Flask serving static website 
- [x] Serve some JSON meta data  
- [ ] Tinker with NN--layers, parameters  

November  
- [ ] Link back end to NN for getting up-to-date info  
- [x] Polish front end design  

December  
- [ ] Clean up work  
- [ ] Reach out to HearthSim to see if they’re interested in this project   

NN Docker Image:  
https://github.com/floydhub/dl-docker  
```
docker run -it -p 8888:8888 -p 6006:6006 -v ~/sharedfolder:/root/sharedfolder floydhub/dl-docker:cpu bash
jupyter notebook --allow-root
```

Flask:  
http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
