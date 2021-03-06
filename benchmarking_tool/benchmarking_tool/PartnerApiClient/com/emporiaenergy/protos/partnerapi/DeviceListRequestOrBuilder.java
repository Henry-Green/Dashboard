// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: partner_api.proto

package com.emporiaenergy.protos.partnerapi;

public interface DeviceListRequestOrBuilder extends
    // @@protoc_insertion_point(interface_extends:protos.DeviceListRequest)
    com.google.protobuf.MessageOrBuilder {

  /**
   * <code>string auth_token = 1;</code>
   * @return The authToken.
   */
  java.lang.String getAuthToken();
  /**
   * <code>string auth_token = 1;</code>
   * @return The bytes for authToken.
   */
  com.google.protobuf.ByteString
      getAuthTokenBytes();

  /**
   * <code>repeated string manufacturer_device_id = 2;</code>
   * @return A list containing the manufacturerDeviceId.
   */
  java.util.List<java.lang.String>
      getManufacturerDeviceIdList();
  /**
   * <code>repeated string manufacturer_device_id = 2;</code>
   * @return The count of manufacturerDeviceId.
   */
  int getManufacturerDeviceIdCount();
  /**
   * <code>repeated string manufacturer_device_id = 2;</code>
   * @param index The index of the element to return.
   * @return The manufacturerDeviceId at the given index.
   */
  java.lang.String getManufacturerDeviceId(int index);
  /**
   * <code>repeated string manufacturer_device_id = 2;</code>
   * @param index The index of the value to return.
   * @return The bytes of the manufacturerDeviceId at the given index.
   */
  com.google.protobuf.ByteString
      getManufacturerDeviceIdBytes(int index);
}
