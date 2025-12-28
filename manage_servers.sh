#!/bin/bash

# Style Transfer Application - Server Management Script

case "$1" in
    start)
        echo "🚀 Starting Style Transfer Application..."
        
        # Start backend
        cd "$(dirname "$0")/backend"
        if [ ! -d "venv" ]; then
            echo "❌ Virtual environment not found. Please run setup first."
            exit 1
        fi
        source venv/bin/activate
        PORT=8000 python app.py > ../backend.log 2>&1 &
        BACKEND_PID=$!
        echo $BACKEND_PID > ../backend.pid
        cd ..
        
        # Wait for backend
        sleep 3
        if curl -s http://localhost:8000/health > /dev/null; then
            echo "✅ Backend started (PID: $BACKEND_PID)"
        else
            echo "⚠️  Backend may still be starting..."
        fi
        
        # Start frontend
        cd frontend
        npm start > ../frontend.log 2>&1 &
        FRONTEND_PID=$!
        echo $FRONTEND_PID > ../frontend.pid
        cd ..
        
        echo "✅ Frontend started (PID: $FRONTEND_PID)"
        echo ""
        echo "🌐 Application URLs:"
        echo "   Frontend: http://localhost:3000"
        echo "   Backend:  http://localhost:8000"
        echo ""
        echo "📝 View logs:"
        echo "   tail -f backend.log"
        echo "   tail -f frontend.log"
        ;;
        
    stop)
        echo "🛑 Stopping servers..."
        
        if [ -f backend.pid ]; then
            kill $(cat backend.pid) 2>/dev/null
            rm backend.pid
            echo "✅ Backend stopped"
        else
            pkill -f "python.*app.py" 2>/dev/null
            echo "✅ Backend stopped (if it was running)"
        fi
        
        if [ -f frontend.pid ]; then
            kill $(cat frontend.pid) 2>/dev/null
            rm frontend.pid
            echo "✅ Frontend stopped"
        else
            pkill -f "react-scripts" 2>/dev/null
            echo "✅ Frontend stopped (if it was running)"
        fi
        ;;
        
    status)
        echo "📊 Server Status:"
        echo ""
        
        if curl -s http://localhost:8000/health > /dev/null 2>&1; then
            echo "✅ Backend: Running on http://localhost:8000"
            curl -s http://localhost:8000/health | python3 -m json.tool 2>/dev/null | sed 's/^/   /'
        else
            echo "❌ Backend: Not running"
        fi
        
        echo ""
        
        if curl -s http://localhost:3000 > /dev/null 2>&1; then
            echo "✅ Frontend: Running on http://localhost:3000"
        else
            echo "❌ Frontend: Not running"
        fi
        ;;
        
    logs)
        case "$2" in
            backend)
                tail -f backend.log
                ;;
            frontend)
                tail -f frontend.log
                ;;
            *)
                echo "📝 Recent logs:"
                echo ""
                echo "=== Backend (last 20 lines) ==="
                tail -20 backend.log 2>/dev/null || echo "No backend log found"
                echo ""
                echo "=== Frontend (last 20 lines) ==="
                tail -20 frontend.log 2>/dev/null || echo "No frontend log found"
                ;;
        esac
        ;;
        
    *)
        echo "Usage: $0 {start|stop|status|logs [backend|frontend]}"
        echo ""
        echo "Commands:"
        echo "  start              Start both backend and frontend servers"
        echo "  stop               Stop both servers"
        echo "  status             Show server status"
        echo "  logs               Show recent logs from both servers"
        echo "  logs backend       Follow backend logs (Ctrl+C to exit)"
        echo "  logs frontend      Follow frontend logs (Ctrl+C to exit)"
        exit 1
        ;;
esac

