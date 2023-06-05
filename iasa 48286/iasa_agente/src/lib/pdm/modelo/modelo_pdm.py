from abc import ABC, abstractmethod


class ModeloPDM(ABC):
    @abstractmethod
    def S(self):
        raise NotImplementedError
    
    @abstractmethod
    def A(self, s):
        raise NotImplementedError
    
    @abstractmethod
    def T(self, s,a, sn):
        raise NotImplementedError
    
    @abstractmethod
    def R(self, s,a,sn):
        raise NotImplementedError
    