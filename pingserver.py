# surprisingly pings the server
import http.client
import time
# Under Testing

def is_http_service_available(host="127.0.0.1", port=80, timeout=1):
    """
    Check if an HTTP service is available on the given host and port.
    """
    try:
        conn = http.client.HTTPConnection(host, port, timeout=timeout)
        conn.request("GET", "/")
        response = conn.getresponse()
        conn.close()
        return response.status < 500  # Consider service available if status is not 5xx
    except Exception as e:
        print(f"Error checking HTTP service on {host}:{port}: {e}")
        return False

def wait_until_available(host="127.0.0.1", port=80, interval=1, timeout=1):
    """
    Wait until the HTTP service on the specified host and port is available.
    """
    while True:
        if is_http_service_available(host, port, timeout):
            print(f"HTTP service on {host}:{port} is available!")
            break
        else:
            print(f"HTTP service on {host}:{port} is not available yet. Retrying in {interval} second(s)...")
            time.sleep(interval)

# Example usage
#wait_until_available(host="127.0.0.1", port=5000)