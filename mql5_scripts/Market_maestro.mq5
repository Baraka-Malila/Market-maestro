//+------------------------------------------------------------------+
//|                                               Market_maestro.mq5 |
//|                                    Copyright 2024, Baraka Malila |
//|                                              bmalila87@gmail.com |
//+------------------------------------------------------------------+
#include <Trade\Trade.mqh>  // Include trading functions-library

// Main parameters with default values-User defined
input double DefaultLots = 0.1;
input int DefaultStopLoss = 200; // in points
input int DefaultTakeProfit = 500; // in points

// Variables for dynamic input from models-
double modelLotSize;
int modelStopLoss;
int modelTakeProfit;
int tradeDirection; // TRADE DIRECTION: 1 for buy, -1 for sell, 0 for no trade

// Fetching signals from Maestro_model (to be integrated)
int GetModelTradeSignal() {
    // TODO: Implement logic to get the model's trade signal
    return 0; // Default to no trade for now
}

// Load trading parameters from defaults or model
void LoadTradingParameters() {
    modelLotSize = DefaultLots; // Replace with model logic if needed
    modelStopLoss = DefaultStopLoss; // Replace with model logic if needed
    modelTakeProfit = DefaultTakeProfit; // Replace with model logic if needed
    tradeDirection = GetModelTradeSignal(); // Get trade direction from your model
}

// Open a position using dynamic or model-supplied parameters(model by override)
void ExecuteTrade(int direction) {
    double price;
    MqlTradeRequest request;
    MqlTradeResult result;
    
    /*I replaced 1, -1 and 0 for BUY, SELL and NO TRADE because the Mql5TradeRequests structure
      calls for an error for undeclared identifier for both the buy and sell OrderSend.
      so the request type in action wil be implemented by ; 0 for BUY and 1 for SELL */

    // For BUY position
    if (direction == 1) {
        price = SymbolInfoDouble(Symbol(), SYMBOL_ASK); // Get Ask price
        request.action = TRADE_ACTION_DEAL;
        request.symbol = Symbol();
        request.volume = modelLotSize;
        request.price = price;
        request.sl = price - modelStopLoss * _Point; // Set Stop Loss
        request.tp = price + modelTakeProfit * _Point; // Set Take Profit
        request.type = 0; // Use 0 for Buy

        if (!OrderSend(request, result)) {
            Print("Error opening Buy order: ", GetLastError());
        }
    } 
    // For SELL position
    else if (direction == -1) { 
        price = SymbolInfoDouble(Symbol(), SYMBOL_BID); // Get Bid price
        request.action = TRADE_ACTION_DEAL;
        request.symbol = Symbol();
        request.volume = modelLotSize;
        request.price = price;
        request.sl = price + modelStopLoss * _Point; // Set Stop Loss
        request.tp = price - modelTakeProfit * _Point; // Set Take Profit
        request.type = 1; // Use 1 for Sell

        if (!OrderSend(request, result)) {
            Print("Error opening Sell order: ", GetLastError());
        }
    }
}

// OnTick function that processes each tick and trades if model suggests
void OnTick() {
    LoadTradingParameters(); // Load dynamic trading logic

    if (tradeDirection != 0) { // Check if the model provided a valid signal (1 or -1)
        ExecuteTrade(tradeDirection);
    }
}
//+------------------------------------------------------------------+
