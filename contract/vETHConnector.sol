pragma solidity 0.4.25; //it's different from asigeng;

contract YMHC{
    mapping (address => uint256) public balanceOf;
    function nbTransfer(address _from, address _to, uint256 _value) public returns (bool success){}
    function getBalance(address _add) public returns (uint256 value){}
    function setBalance(address _add, uint256 _value) public returns (bool success) {}
}

contract vETH{
    mapping (address => uint256) public  balanceOf;
    function nbTransfer(address _from, address _to, uint256 _value) public returns (bool success){}
    function getBalance(address _add) public returns (uint256 value){}
    function setBalance(address _add, uint256 _value) public returns (bool success) {}
}


contract vETHConnector {
    YMHC instance;
    vETH reserve ;
    uint256 constant CW = 5e7 ;  //Connector Weight
    uint256 constant Const = 1e8;  //multiple
    uint256 ratio = 1e8;  // initial ratio
    uint256 beforeTrade =1e7 ; // the price befor trading
    
    address yAddress = 0x72673e92ae4033682321705342785919676DcD3B;
    address vAddress = 0x3B6082940394D8150a6229A9FFDea9417785E32c;
    
    event Test(address _from, uint ratio);
    
    function sqrt(uint x) private returns (uint y) {
    uint z = (x + 1) / 2;
    y = x;
    while (z < y) {
        y = z;
        z = (x / z + z) / 2;
        }
    }
    

    function vETHConnector() public {
        instance = YMHC(yAddress);
        reserve = vETH(vAddress);
    }
    

    function getValue() external returns(uint256 propation){
        return ratio ;
    }
    
    function buySmartToken(address _from , uint256 _value) returns (uint256 value){ //return smart token
        uint result= instance.getBalance(this)*(sqrt(1 + _value / reserve.getBalance(this)) - 1);
        instance.nbTransfer(this , _from , result);
        reserve.nbTransfer(_from , this ,_value);
        Test(_from, ratio);
        
        beforeTrade = _value / result * Const;
        ratio = reserve.getBalance(this) / ( (CW/Const)* instance.getBalance(this) ) * Const;
       
        return result;
    }
    
    function buyVETH (address _from , uint256 _value) returns (uint256 value){ // return the number of vETH
        uint result= reserve.getBalance(this)*((1 + _value / instance.getBalance(this))*(1 + _value / instance.getBalance(this)) - 1);
        reserve.nbTransfer(this , _from , result);
        instance.nbTransfer(_from , this ,_value);
        
        beforeTrade = result / _value * Const;
        ratio = reserve.getBalance(this) / ( (CW/Const)* instance.getBalance(this) ) * Const;
        return result;
    }
} 